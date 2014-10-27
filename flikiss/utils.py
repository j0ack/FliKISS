#! /usr/bin/env python
#-*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

"""
    Utilities for FliKISS app
    ~~~~~~~~~~~~~~~~~~~~~~~~~
"""

__author__ = u'TROUVERIE Joachim'

from markdown import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree


class InterWikiLinksPattern(Pattern):
    """
        Pattern to add an inter wiki links extension to markdown
    """
    def handleMatch(self, m):
        label = m.group(2).strip()
        a = etree.Element('a')
        text = None
        # get label
        if '|' in label :
            text = label.split('|')[1]
            label = label.split('|')[0]
        # get url
        if ':' in label :
            page = label.split(':')[1]
            base_url = label.split(':')[0]            
            a.text = text or page
            a.set('href', '/{0}/?page={1}'.format(base_url, page))
        else :
            a.text = text or label
            a.set('href', '/?page={0}'.format(label))
        return a
            

class InterWikiLinksExtension(Extension) :
    """
        Inter wiki links extension for Markdown
        
        It is possible to use it to reference other category page
        
          [[category:test_page]]
          <a href="/category/?page=test_page">test_page</a>
    """
    def extendMarkdown(self, md, md_globals):
        WIKILINK_RE = r'\[\[([\w0-9_ -:\|]+)\]\]'
        pattern = InterWikiLinksPattern(WIKILINK_RE)
        md.inlinePatterns.add('interwikilink', pattern, "<not_strong")


class CenterAlignPattern(Pattern):
    """
        Pattern to center elements
    """
    def handleMatch(self,m):
        div = etree.Element('div')
        div.set('style','display:block;text-align:center;')
        div.text = m.group(3)
        return div


class RightAlignPattern(Pattern):
    """
        Pattern to right elements
    """    
    def handleMatch(self,m):
        div = etree.Element('div')
        div.set('style','display:block;text-align:right;')
        div.text = m.group(3)
        return div


class AlignExtension(Extension):
    """
        Align extension for Markdown
        
        Center or align to right elements
        -> center element <-
        -> align to right element ->
    """
    def extendMarkdown(self, md, md_globals):       
        CENTR_RE = r'(\-\>)(.+?)(\<\-)'
        RIGHT_RE = r'(\-\>)(.+?)(\-\>)'
        center_pattern = CenterAlignPattern(CENTR_RE)
        right_pattern = RightAlignPattern(RIGHT_RE)
        md.inlinePatterns.add('CenterAlign', center_pattern, "<not_strong")
        md.inlinePatterns.add('RightAlign', right_pattern, "<not_strong")


def render_markdown(content) :
    """
        Translate markdown to HTML

        :param content: markdown content
    """
    return markdown(content, extensions=['codehilite','tables',
                             'admonition', InterWikiLinksExtension(),
                             AlignExtension()])


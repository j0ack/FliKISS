/***
* JavaScript for Markdown Editor
* https://github.com/lepture/editor/blob/master/src/intro.js
* author : Hsiaoming Yang
**/

/**
* Get state of editor
**/
function _getState(cm, pos) {
  pos = pos || cm.getCursor('start');
  var stat = cm.getTokenAt(pos);
  if (!stat.type) return {};

  var types = stat.type.split(' ');

  var ret = {}, data, text;
  for (var i = 0; i < types.length; i++) {
    data = types[i];
    if (data === 'strong') {
      ret.bold = true;
    } 
    else if (data === 'em') {
      ret.italic = true;
    }
  }
  return ret;
}

/**
* Replace text in editor
**/
function _replaceSelection(cm, start, end) {
  var startPoint = cm.getCursor('start');
  var endPoint = cm.getCursor('end');
  
  var text = cm.getSelection();
  cm.replaceSelection(start + text + end);

  startPoint.ch += start.length;
  endPoint.ch += start.length;
  
  cm.setSelection(startPoint, endPoint);
  cm.focus();
}


/**
* Set text to bold
**/
function toggleBold(editor) {
  var stat = _getState(editor);

  var text;
  var start = '**';
  var end = '**';

  var startPoint = editor.getCursor('start');
  var endPoint = editor.getCursor('end');
  if (stat.bold) {
    text = editor.getLine(startPoint.line);
    start = text.slice(0, startPoint.ch);
    end = text.slice(startPoint.ch);

    start = start.replace(/^(.*)?(\*|\_){2}(\S+.*)?$/, '$1$3');
    end = end.replace(/^(.*\S+)?(\*|\_){2}(\s+.*)?$/, '$1$3');
    startPoint.ch -= 2;
    endPoint.ch -= 2;
    editor.setLine(startPoint.line, start + end);
  } 
  
  else {
    text = editor.getSelection();
    editor.replaceSelection(start + text + end);

    startPoint.ch += 2;
    endPoint.ch += 2;
  }

  editor.setSelection(startPoint, endPoint);
  editor.focus();
}

/**
* Set text to italic
**/
function toggleItalic(editor) {
  var stat = _getState(editor);

  var text;
  var start = '*';
  var end = '*';

  var startPoint = editor.getCursor('start');
  var endPoint = editor.getCursor('end');
  if (stat.bold) {
    text = editor.getLine(startPoint.line);
    start = text.slice(0, startPoint.ch);
    end = text.slice(startPoint.ch);

    start = start.replace(/^(.*)?(\*|\_)(\S+.*)?$/, '$1$3');
    end = end.replace(/^(.*\S+)?(\*|\_)(\s+.*)?$/, '$1$3');
    startPoint.ch -= 1;
    endPoint.ch -= 1;
    editor.setLine(startPoint.line, start + end);
  } 

  else {
    text = editor.getSelection();
    editor.replaceSelection(start + text + end);

    startPoint.ch += 1;
    endPoint.ch += 1;
  } 

  editor.setSelection(startPoint, endPoint);
  editor.focus();
}

/**
* Action for drawing a link.
*/
function drawLink(editor) {
  var stat = _getState(editor);
  _replaceSelection(editor, '[', '](http://)');
}


/**
* Action for drawing an img.
*/
function drawImage(editor) {
  var stat = _getState(editor);
  _replaceSelection(editor, '![', '](/<your_file_url>)');
}

/**
 * Action to toggle preview
 **/
function togglePreview(editor, convert_url) {
  var wrapper = editor.getWrapperElement();
  var preview = document.getElementById('markdown_preview');
  var btn = document.getElementById('preview_btn');
  if (wrapper.style.display != 'none') {
    // send request to server with value
    btn.className = btn.className.replace('fa-eye', 'fa-spin fa-spinner');
    var text = editor.getValue();
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
      if (httpRequest.readyState === 4) {
        if (httpRequest.status === 200) {
          var data = JSON.parse(httpRequest.responseText);
          preview.innerHTML = data.value;
          preview.style.display = 'block';
          wrapper.style.display = 'none';
          btn.className = btn.className.replace('fa-spin fa-spinner', 'fa-eye-slash');
        }
      }
    };
    httpRequest.open('POST', convert_url);
    httpRequest.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    httpRequest.send('content=' + text); 
  }
  else {
    preview.style.display = 'none';
    wrapper.style.display = 'block';
    btn.className = btn.className.replace('fa-eye-slash', 'fa-eye');
  }   
}   


/**
 * Draw toolbar for editor
 **/
function drawToolbar(editor, convert_url) {
    var container = document.createElement('div');
    container.className = 'toolbar';
    // bold
    var bold = document.createElement('span');
    bold.className = 'fa fa-bold';
    bold.onclick = function(evt) {
        toggleBold(editor);
    }
    container.appendChild(bold);
    // italic
    var italic = document.createElement('span');
    italic.className = 'fa fa-italic';
    italic.onclick = function(evt) {
        toggleItalic(editor);
    }
    container.appendChild(italic);
    // img
    var img = document.createElement('span');
    img.className = 'fa fa-photo'
    img.onclick = function(evt) {
        drawImage(editor);
    }
    container.appendChild(img);
    // link
    var link = document.createElement('span');
    link.className = 'fa fa-link';
    link.onclick = function(evt) {
        drawLink(editor);
    }
    container.appendChild(link);
    // preview
    var preview = document.createElement('span');
    preview.onclick = function(evt) {
        togglePreview(editor, convert_url);
    }
    preview.setAttribute('id', 'preview_btn');
    preview.className = 'fa fa-eye';
    container.appendChild(preview);

    // append container
    var wrapper = editor.getWrapperElement();
    wrapper.parentNode.insertBefore(container, wrapper);
}

/**
 * Insert preview div
 **/
function drawPreview(editor) {
    var wrapper = editor.getWrapperElement();
    var preview = document.createElement('div');
    preview.setAttribute('id', 'markdown_preview');
    preview.style.display = 'none';
    wrapper.parentNode.insertBefore(preview, wrapper.nextSibling);
}


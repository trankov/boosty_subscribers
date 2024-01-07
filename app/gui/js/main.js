const btnFile = document.getElementById('btnFile');
const btnFetch = document.getElementById('btnFetch');

btnFile.addEventListener('click', (evt) => send_event('btnFile', 'click'))
btnFetch.addEventListener('click', (evt) => send_event('btnFetch', 'click'))

function send_event(sender, ev) {
    eel.resolve_event(sender, ev);
}

eel.expose(change_content);
function change_content(elementId, content) {
    document.getElementById(elementId).innerHTML = content;
}

eel.expose(change_style);
function change_style(elementId, style) {
    document.getElementById(elementId).style = style;
}

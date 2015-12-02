var editor, $tb;

function make_editor(el, opts) {
    var config = {
        lineNumbers: true,
        lineWrapping: true,
        autoClearEmptyLines: true,
        matchBrackets: true,
        mode: opts.mode || 'text/css'
    };
    django.jQuery.extend(config, opts);
    editor = CodeMirror.fromTextArea(document.getElementById(el), config);
    $editor = django.jQuery(editor.getWrapperElement());
    $tb = django.jQuery('<div class="cm-toolbar" not-content="true">');
    $editor.prepend($tb);
}

function add_button(opts) {
    var $el = django.jQuery('<button type="button" class="grp-button" title="' + opts.title + '">' + opts.label + '</button>');
    $el.on('click', opts.action);
    $tb.append($el);
}

function reindent () {
    var sel = editor.somethingSelected(),
        i = sel ? editor.getCursor().line : 0,
        l = sel ? editor.getCursor(false).line : editor.lineCount();

    for( ; i < l ; i++ ) {
        var row = editor.getLine(i).replace(/^\s\s*/, '').replace(/\s\s*$/, '');
        editor.indentLine(i);
    }
};


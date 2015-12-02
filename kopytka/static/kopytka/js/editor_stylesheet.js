django.jQuery(document).ready(function () {
    try {
        editor = make_editor('id_source', {mode: 'text/x-scss'});
        add_button({
            title: 'Reindent',
            action: reindent,
            label: '&raquo;'
        });
    } catch (err) {}
});

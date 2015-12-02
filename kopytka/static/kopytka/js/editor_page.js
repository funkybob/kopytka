django.jQuery(document).ready(function () {
    try {
        editor = make_editor('id_content', {mode: 'text/x-django'});
        add_button({
            title: 'Reindent',
            action: reindent,
            label: '&raquo;'
        });
    } catch (err) {}
});

(function($) {
    'use strict';

    function make_row(k, v) {
        k = k || '';
        v = v || '';
        return  '<tr class="form-row"' + ((k === '') ? '' : ' data-value="' + encodeURIComponent(v) + '"') + '>' +
                    '<td><input type="text" value="' + k + '"></td>' +
                    '<td><textarea class="vLargeTextField">' + v + '</textarea></td>' +
                    '<td><a class="inline-deletelink">Delete</a></td>' +
                '</tr>' ;
    }

    $.fn.hstore = function () {
        this.each(function () {
            var $field = $(this);
            var $el = $field.parent();

            // parse the data - save the original
            var data = JSON.parse($field.val() || '{}');
            // hide the text area
            $field.hide();

            // generate list of (input : textarea) widgets
            $el.append(
                '<div class="inline-group">' +
                    '<div class="tabular inline-related">' +
                        '<table>' +
                            '<thead><tr><th>Name</th><th>Value</th><th></th></tr></thead>' +
                            '<tfoot><tr class="add-row"><td colspan=3><a href="#">Add another</a></td></tr></tfoot>' +
                            '<tbody></tbody>' +
                        '</table>' +
                    '</div>' +
                '</div>'
            );
            var $container = $el.find('tbody');
            Object.keys(data).sort().forEach(function (k) {
                $container.append(make_row(k, data[k]));
            });

            // Add add/remove/revert buttons
            $el.find('.add-row a').on('click', function (ev) {
                $container.append(make_row());
                ev.preventDefault();
            });

            $container.on('click', '.inline-deletelink', function () {
              var $el = $(this).closest('tr.form-row');
              if($el.data('value')) {
                // mark for deletion
              } else {
                // remove
                $el.remove();
              }
            });

            // hook into submit action
            var $form = $el.closest('form');
            $form.on('submit', function (ev) {
                // build a new data object
                var d = {};
                $container.find('input').each(function (el) {
                    var key = $(this).val();
                    var val = $(this).closest('tr').find('textarea').val();
                    if(val && key) { d[key] = val; }
                });
                // update the input
                $field.val(JSON.stringify(d));
            });
        });
        return this;
    };

    $(document).ready(function () {
        $('textarea.hstore').hstore();
    });
})(django.jQuery);

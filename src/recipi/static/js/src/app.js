import jquery from 'jquery';
import Backbone from 'backbone';
import Foundation from 'foundation';
import brace from 'brace';
import * as markdown from 'brace/mode/markdown';
import * as monokai from 'brace/theme/monokai';

$(() => {
	Backbone.$ = $;
	Backbone.history.start({pushState: true});

	Foundation.init();

    var editor = ace.edit('editor');

    editor.setTheme('ace/theme/monokai');
    editor.getSession().setMode('ace/mode/markdown');
    editor.setAutoScrollEditorIntoView(true);
    editor.setOption('maxLines', 150);

    console.log("initialized!", editor);
});

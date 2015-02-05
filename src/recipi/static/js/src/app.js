import jquery from 'jquery';
import Backbone from 'backbone';
import Foundation from 'foundation';
import brace from 'brace';
import * as markdown from 'brace/mode/markdown';
import * as monokai from 'brace/theme/kuroir';

$(() => {
	Backbone.$ = $;
	Backbone.history.start({pushState: true});

	Foundation.init();

    var editor = ace.edit('editor');

    editor.setTheme('ace/theme/kuroir');
    editor.getSession().setMode('ace/mode/markdown');
    editor.setAutoScrollEditorIntoView(true);
    editor.getSession().setUseWrapMode(true);
    editor.getSession().setTabSize(4);
    editor.getSession().setUseSoftTabs(true);

    editor.setBehavioursEnabled(true);
    editor.setHighlightSelectedWord(true);
    editor.setHighlightActiveLine(true);
    editor.setDisplayIndentGuides(true);
    editor.setShowPrintMargin(false);
    editor.setFontSize(16);

    editor.setOption('maxLines', 150);

    console.log("initialized!", editor);
});

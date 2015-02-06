import $ from 'jquery';
import Backbone from 'backbone';
import Foundation from 'foundation';
import brace from 'brace';
import * as markdown from 'brace/mode/markdown';
import * as monokai from 'brace/theme/kuroir';

$(() => {
    console.log('Initialize backbone...');

	Backbone.$ = $;
	Backbone.history.start({pushState: true});

    console.log('Initialize foundation...');
	Foundation.init();

    if ($('.editor').length > 0) {
        console.log('Initialize ACE editor...');
        var editor = ace.edit($('.editor')[0]);

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
    }

    console.log('Initialized!');
});

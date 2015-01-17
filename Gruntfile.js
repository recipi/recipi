module.exports = function(grunt) {
	var appConfig = grunt.file.readJSON('package.json');

	// Load grunt tasks automatically
	// see: https://github.com/sindresorhus/load-grunt-tasks
	require('load-grunt-tasks')(grunt);

	// Time how long tasks take. Can help when optimizing build times
	// see: https://npmjs.org/package/time-grunt
	require('time-grunt')(grunt);

	var to5Browserify = require('6to5ify');

	var pathsConfig = function (appName) {
		this.app = appName || appConfig.name;

		return {
			app: this.app,
			foundation_scss: this.app + '/../../node_modules/zurb-foundation-5/scss/',
			templates: this.app + '/templates',
			css: this.app + '/static/css',
			sass: this.app + '/static/scss',
			fonts: this.app + '/static/fonts',
			images: this.app + '/static/img',
			js: this.app + '/static/js'
		};
	};

	grunt.initConfig({
		pkg: appConfig,
		paths: pathsConfig('src/recipi'),

		browserify: {
			app: {
				src: '<%= paths.js %>/src/app.js',
				dest: '<%= paths.js %>/build/app.js',
				options: {
					extensions: ['.js', '.html'],
					transform: [
						'browserify-shim',
						[to5Browserify, {
							sourceMap: true,
							eperimental: true
						}],
						'hbsfy'
					],
					watch: true,
					keepAlive: false,
				},
			}
		},
		sass: {
			options: {
				sourceMap: true,
				includePaths: ['<%= paths.foundation_scss %>'],
			},
			dist: {
				options: {
					outputStyle: 'expanded'
				},

				files: [{
					expand: true,
					cwd: '<%= paths.sass %>',
					src: ['app.scss'],
					dest: '<%= paths.css %>',
					ext: '.css'
				}]
			}
		},
		watch: {
			options: {
				livereload: true,
			},
			sass: {
				files: [
					'<%= paths.sass %>/**/*'
				],
				tasks: ['sass']
			},
			app: {
				files: ['<%= paths.js %>/build/**/*'],
				tasks: []
			}
		},
		lintspaces: {
			all: {
				src: [
					'<%= paths.js %>',
					'<%= paths.sass %>'
				],
				options: {
					editorconfig: '.editorconfig'
				}
			},
			javascript: {
				src: ['<%= paths.js %>/src/*.js'],
				options: {
					editorconfig: '.editorconfig'
				}
			},
			external: {
				src: [
					'<%= paths.app %>/**/*',
					'!<%= paths.app %>/static/*.ico',
					'!<%= paths.images %>/*',
					'!<%= paths.fonts %>/*',
					'!<%= paths.js %>/src/libs/*',
					'!<%= paths.js %>/build/*',
					'!<%= paths.js %>/vendor/*',
					'!<%= paths.css %>/**',
					'!<%= paths.app %>/**/djangojs.js',
					'!<%= paths.app %>/**/django.pot',
					'!<%= paths.app %>/**/django.po',
					'!<%= paths.app %>/resources/**',
					'!<%= paths.app %>/tests/resources/**',
					'!<%= paths.app %>/**/*.py'
				],
				options: {
					editorconfig: '.editorconfig'
				}
			}
		},
		jshint: {
			all: ['Gruntfile.js', '<%= paths.js %>/*.js']
		},
		jscs: {
			all: {
				options: {
					'standard': 'Jquery'
				},
				files: {
					src: ['tasks']
				}
			}
		},
		clean: {
			build: {
				src: [
					'<%= paths.js %>/build/**/*',
					'<%= paths.css %>/**/*'
				]
			}
		},
	});

	grunt.registerTask(
		'default',
		'Run all tasks in a row.',
		['build']
	);

	grunt.registerTask(
		'validate',
		'Validate all files.',
		['jshint', 'jscs', 'lintspaces']
	);

	grunt.registerTask(
		'test',
		'Run JS tests.',
		[]
	);

	grunt.registerTask(
		'build',
		'Build all JS files for a deploy.',
		['validate', 'clean:build', 'browserify', 'sass']
	);

	grunt.registerTask(
		'devbuild',
		'Build all JS files for a deploy.',
		['browserify', 'sass']
	);

	grunt.registerTask('serve', [
		'sass',
		'browserify',
		'watch'
	]);
};

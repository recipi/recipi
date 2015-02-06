var gulp = require('gulp'),
	del = require('del'),
	plugins = require('gulp-load-plugins')(),
	livereload = require('gulp-livereload'),
	gutil = require('gulp-util'),
	source = require('vinyl-source-stream'),
	buffer = require('vinyl-buffer'),
	browserify = require('browserify'),
	to5ify = require('6to5ify'),
	uglify = require('gulp-uglify'),
	watchify = require('watchify'),
	read = require('fs').readFileSync,
	base = './src/recipi',
	src = {
		foundation: 'bower_components/foundation/scss',
		templates: base + '/templates',
		scss: base + '/static/scss',
		fonts: base + '/static/fonts',
		images: base + '/static/img',
		js: base + '/static/js',
		manageScript: 'manage.py'
	},
	dest = {
		css: base + '/static/css',
		js: base + '/static/js/build'
	};

/**
 * Cleaning css directory
 */
gulp.task('clean:css', function (done) {
	del(dest.css, done);
});

/**
 * Cleaning js directory
 */
gulp.task('clean:js', function (done) {
	del(dest.js, done);
});

/**
 * Compiling sass/scss files to css
 */
gulp.task('scss', ['clean:css'], function () {
	return gulp.src(src.scss + '/*.scss')
		.pipe(plugins.plumber())
		.pipe(plugins.sourcemaps.init())
		.pipe(plugins.sass({
			includePaths: [src.foundation]
		}))
		.pipe(plugins.sourcemaps.write('./'))
		.pipe(gulp.dest(dest.css))
		.pipe(livereload());
});

/**
* Validating scss files
*/
gulp.task('validate:scss', function () {
	return gulp.src(src.scss + '/**/*.scss')
		.pipe(plugins.plumber())
		.pipe(plugins.lintspaces())
		.pipe(plugins.lintspaces.reporter());
});

/**
* Validating js files
*/
gulp.task('validate:js', function () {
	return gulp.src(src.js + '/*.js')
		.pipe(plugins.plumber())
		.pipe(plugins.jscs({
			preset: 'jquery'
		}))
		.pipe(plugins.jshint())
		.pipe(plugins.lintspaces())
		.pipe(plugins.lintspaces.reporter());
});

/**
* Building our javascript files
*/
gulp.task('js', function() {
	browserify(src.js + '/src/app.js', watchify.args)
		.transform(to5ify)
		.bundle({debug: true})
		.on('error', gutil.log.bind(gutil, 'Browserify Error'))
		.pipe(source('bundle.js'))
		.pipe(buffer())
		.pipe(plugins.sourcemaps.init({loadMaps: true}))
		.pipe(uglify())
		.pipe(plugins.sourcemaps.write('./'))
		.pipe(gulp.dest(src.js + '/build'))
		.pipe(livereload());
});


var bundler = watchify(browserify(src.js + '/src/app.js', watchify.args));

bundler.transform(to5ify);

gulp.task('jjs', bundle);
bundler.on('update', bundle);


function bundle() {
	return bundler.bundle()
		.on('error', gutil.log.bind(gutil, 'Browserify Error'))
		.pipe(source('bundle.js'))
		.pipe(gulp.dest(src.js + '/build'))
		.pipe(livereload());
}


/**
* Validating files
*/
gulp.task('validate', ['validate:scss', 'validate:js']);

gulp.task('watch', function () {
	gulp.watch(src.js + '/src/*.js', ['validate:js', 'jjs']);
	gulp.watch(src.scss + '/**/*.scss', ['validate:scss', 'scss']);
	livereload.listen();
});

gulp.task('build', ['validate', 'js', 'scss']);

gulp.task('default', ['build']);

gulp.task('serve', ['validate', 'scss', 'jjs', 'watch'], plugins.shell.task([
	'env PYTHONUNBUFFERED=true python ' + src.manageScript + ' runserver',
	'env PYTHONUNBUFFERED=true celery worker -A recipi.core.tasks -l INFO -E',
	])
);

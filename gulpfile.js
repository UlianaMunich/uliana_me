
////////////////////////////////
		//Setup//
////////////////////////////////

// Plugins
var gulp = require('gulp'),
      pjson = require('./package.json'),
      gutil = require('gulp-util'),
      sass = require('gulp-sass'),
      autoprefixer = require('gulp-autoprefixer'),
      cleanCSS = require('gulp-clean-css');
      jshint = require('gulp-jshint'),
      uglify = require('gulp-uglify'),
      imagemin = require('gulp-imagemin'),
      rename = require('gulp-rename'),
      concat = require('gulp-concat'),
      runSequence = require('run-sequence'),
      exec = require('child_process').exec,
      bower = require('gulp-bower'),
      browserSync = require('browser-sync').create(),
      reload = browserSync.reload;


// Relative paths function
var pathsConfig = function (appName) {
  this.app = "./" + (appName || pjson.name);

  return {
    app: this.app,
    templates: this.app + '/templates',
    css: this.app + '/static/css',
    sass: this.app + '/static/sass',
    fonts: this.app + '/static/fonts',
    images: this.app + '/static/images',
    js: this.app + '/static/js',
    jsLibs: [
      this.app + '/static/js/libs.js',
      this.app + '/static/js/app.js',
      ],
    fonts: this.app + '/static/fonts',
    fontLibs: [
      'bower_components/font-awesome/fonts/fontawesome-webfont.*',
    ]
  }
};

var paths = pathsConfig();

////////////////////////////////
		//Tasks//
////////////////////////////////

// Styles
gulp.task('styles', function() {
  return gulp.src(paths.sass + '/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer('last 2 version'))
    .pipe(gulp.dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(cleanCSS())
    .pipe(gulp.dest(paths.css));
});

// Fonts
gulp.task('fonts', function() {
  return gulp.src(paths.fontLibs)
       .pipe(gulp.dest(paths.fonts));
});

// Scripts
gulp.task('scripts', function() {
  return gulp.src(paths.jsLibs)
    .pipe(concat('main.js'))
    .pipe(gulp.dest(paths.js))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify({preserveComments:'some'}))
    .pipe(gulp.dest(paths.js));
});

gulp.task('images', function(){
  return gulp.src(paths.images + '/**/*')
    .pipe(imagemin())
    .pipe(gulp.dest(paths.images))
});

// Run django server
gulp.task('runServer', function() {
  exec('python manage.py runserver', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
});

// Install bower packages
gulp.task('bower', function() {
  return bower();
});

// Build static files
gulp.task('build', function() {
  runSequence('bower', 'fonts', 'styles', 'scripts');
});

// Browser sync server for live reload
gulp.task('browserSync', function() {
    browserSync.init(
      [paths.css + "/*.css", paths.js + "*.js", paths.templates + '*.html'], {
        proxy:  "localhost:8000"
    });
});

// Default task
gulp.task('default', function() {
    runSequence(['styles', 'scripts', 'images'], 'runServer', 'browserSync');
});

////////////////////////////////
		//Watch//
////////////////////////////////

// Watch
gulp.task('watch', ['default'], function() {

  gulp.watch(paths.sass + '/*.scss', ['styles']);
  gulp.watch(paths.js + '/app.js', ['scripts']).on("change", reload);
  gulp.watch(paths.images + '/*', ['images']);
  gulp.watch(paths.templates + '/**/*.html').on("change", reload);

});

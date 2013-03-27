'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives']).
    config(['$routeProvider', function($routeProvider) {
        // welcome
        $routeProvider.when('/welcome', {templateUrl: 'static/page/welcome.html'});
        // sizheninfo   
        $routeProvider.when('/drug', {templateUrl: 'static/page/drug.html', controller: drugCtrl});
        
        $routeProvider.when('/fixedrecipe', {templateUrl: 'static/page/fixedrecipe.html', controller:fixedrecipeCtrl});
        
        $routeProvider.when('/wdisease', {templateUrl: 'static/page/wdisease.html', controller: wdiseaseCtrl});
       
        $routeProvider.when('/cdisease', {templateUrl: 'static/page/cdisease.html', controller: cdiseaseCtrl});
        
        $routeProvider.when('/semiotic', {templateUrl: 'static/page/semiotic.html', controller: semioticCtrl});
        // addinfo
        $routeProvider.when('/dmethod', {templateUrl: 'static/page/dmethod.html', controller: dmethodCtrl});
        
        $routeProvider.when('/symptom', {templateUrl: 'static/page/symptom.html', controller: symptomCtrl});
        // sizhen connect action
        
        $routeProvider.when('/dtemplate', {templateUrl: 'static/page/dtemplate.html', controller: dtemplateCtrl});
        
        $routeProvider.when('/examination', {templateUrl: 'static/page/examination.html', controller: examinationCtrl});
       
        $routeProvider.when('/analysis-sample-view/:analysisType', {templateUrl: 'static/page/analysis-sample-view.html', controller: AnalysisSampleCtrl});
        // otherwise
        $routeProvider.otherwise({redirectTo: '/welcome'});
    }]);

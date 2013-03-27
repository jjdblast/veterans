'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives']).
    config(['$routeProvider', function($routeProvider) {
        // welcome
        $routeProvider.when('/welcome', {templateUrl: 'static/page/welcome.html'});
        // sizheninfo   
        $routeProvider.when('/drugMgr', {templateUrl: 'static/page/drugMgr.html', controller: drugMgrCtrl});
        
        $routeProvider.when('/fixedrecipeMgr', {templateUrl: 'static/page/fixedrecipeMgr.html', controller:fixedrecipeMgrCtrl});
        
        $routeProvider.when('/wdiseaseMgr', {templateUrl: 'static/page/wdiseaseMgr.html', controller: wdiseaseMgrCtrl});
       
        $routeProvider.when('/cdiseaseMgr', {templateUrl: 'static/page/cdiseaseMgr.html', controller: cdiseaseMgrCtrl});
        
        $routeProvider.when('/semioticMgr', {templateUrl: 'static/page/semioticMgr.html', controller: semioticMgrCtrl});
        // addinfo
        $routeProvider.when('/dmethodMgr', {templateUrl: 'static/page/dmethodMgr.html', controller: dmethodMgrCtrl});
        
        $routeProvider.when('/symptomMgr', {templateUrl: 'static/page/symptomMgr.html', controller: symptomMgrCtrl});
        // sizhen connect action
        
        $routeProvider.when('/dtemplateMgr', {templateUrl: 'static/page/dtemplateMgr.html', controller: dtemplateMgrCtrl});
        
        $routeProvider.when('/examinationMgr', {templateUrl: 'static/page/examinationMgr.html', controller: examinationMgrCtrl});
       
        $routeProvider.when('/analysis-sample-view/:analysisType', {templateUrl: 'static/page/analysis-sample-view.html', controller: AnalysisSampleCtrl});
        // otherwise
        $routeProvider.otherwise({redirectTo: '/welcome'});
    }]);

'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives']).
    config(['$routeProvider', function($routeProvider) {
        // welcome
        $routeProvider.when('/welcome', {templateUrl: 'static/page/welcome.html'});
        // sizheninfo
        $routeProvider.when('/sizheninfo-list-view', {templateUrl: 'static/page/sizheninfo-list-view.html', controller: SizhenInfoListCtrl});
        $routeProvider.when('/sizheninfo-detail-view/:patientID', {templateUrl: 'static/page/sizheninfo-detail-view.html', controller: SizhenInfoDetailCtrl});
        // addinfo
        $routeProvider.when('/addinfo-list-view', {templateUrl: 'static/page/addinfo-list-view.html', controller: AddInfoListCtrl});
        $routeProvider.when('/addinfo-detail-view/:patientID', {templateUrl: 'static/page/addinfo-detail-view.html', controller: AddInfoDetailCtrl});
        // sizhen connect action
        $routeProvider.when('/sizheninfo-connect-view/:sizheninfoID/:addinfoID', {templateUrl: 'static/page/sizheninfo-connect-view.html', controller: SizhenInfoConnectCtrl});
        $routeProvider.when('/sizheninfo-connect-selection-view', {templateUrl: 'static/page/sizheninfo-connect-selection-view.html', controller: AddInfoListCtrl});
        // analysis sample
        $routeProvider.when('/analysis-sample-view/:analysisType', {templateUrl: 'static/page/analysis-sample-view.html', controller: AnalysisSampleCtrl});
        // otherwise
        $routeProvider.otherwise({redirectTo: '/welcome'});
    }]);

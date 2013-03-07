'use strict';

/* Services */

var myAppService = angular.module('myApp.services', ['ngResource']);

myAppService.factory('SizhenInfo', function($resource){
    return $resource(
        //'static/mockdata/sizheninfo-:patientID.json',
        '/api/sizheninfo',
        {},
        {
            query: {
                method:'GET',
                //params:{patientID:'list'},
                isArray:true
            }
        }
    );
});

myAppService.factory('DrugInfo', function($resource){
    return $resource(
        //'static/mockdata/sizheninfo-:patientID.json',
        '/api/sizheninfo',
        {},
        {
            query: {
                method:'GET',
                //params:{patientID:'list'},
                isArray:true
            }
        }
    );
});

myAppService.factory('WdiseaseInfo', function($resource){
    return $resource(
        //'static/mockdata/sizheninfo-:patientID.json',
        '/api/sizheninfo',
        {},
        {
            query: {
                method:'GET',
                //params:{patientID:'list'},
                isArray:true
            }
        }
    );
});

myAppService.factory('AddInfo', function($resource){
    return $resource(
        'static/mockdata/addinfo-:patientID.json',
        {},
        {
            query: {
                method:'GET',
                params:{patientID:'list'},
                isArray:true
            }
        }
    );
});


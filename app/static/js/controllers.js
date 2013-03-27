'use strict';

/* Controllers */


function TestCtrl($scope) {
    $scope.test = ["yan","xing"];
}

function drugCtrl($scope, $routeParams) {
    $scope.drug_list = [
        { "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"},{ "code":"1895", "name":"川乌", "unit":"克", "alias":" ", "py":"cw", "wb":"kq", "isClassical":"1", "SPETid":" ", "illustration":"","state":"3"}]
}
function fixedrecipeCtrl($scope, $routeParams) {
    $scope.fixedrecipe_list = [ {"name":"2", "code":"2", "effect":"2",  "isClassical":"2", "SPETid":"2", "py":"2", "wb":"2", "state":"2"}]
} 

function cdiseaseCtrl($scope, $routeParams) {
    $scope.cdisease_list = [ {"name":"3", "code":"3", "level":"3" ,"isClassical":"3", "SPETid":"3",  "state":"3"}]
}

function wdiseaseCtrl($scope, $routeParams) {
    $scope.wdisease_list = [ {"name":"4", "code":"4", "unit":"4", "alias":"4","isClassical":"4", "SPETid":"4",  "state":"4"}]
}

function semioticCtrl($scope, $routeParams) {
    $scope.semiotic_list = [ {"code":"5", "name":"5", "isClassical":"5", "SPETid":"5",  "state":"5"}]
}

function dmethodCtrl($scope, $routeParams) {
    $scope.dmethod_list = [ {"method":"6", "code":"6","level":"6", "isClassical":"6", "SPETid":"6",  "state":"6"}]
}

function symptomCtrl($scope, $routeParams) {
    $scope.symptom_list = [ {"name":"7","method":"7", "code":"7","level":"7","class":"7", "isClassical":"7", "SPETid":"7",  "state":"7"}]
}

function dtemplateCtrl($scope, $routeParams) {
    $scope.dtemplate_list = [ {"name":"8", "code":"8","SPETid":"8","WDISid":"8","state":"8"}]
}

function examinationCtrl($scope, $routeParams) {
    $scope. examination_list = [ {"name":"9", "code":"9","class":"9","isClassical":"9","SPETid":"9","state":"9"}]
}


function AnalysisSampleCtrl($scope, $routeParams) { 
    switch($routeParams.analysisType) {
        case "plotPhysique":
            $scope.$on('$viewContentLoaded', plotPhysique);
            break;
        case "medicineBasic":
            $scope.$on('$viewContentLoaded', medicineBasic);
            break;
        case "healthBasic":
            $scope.$on('$viewContentLoaded', healthBasic);
            break;
        default:
            alert("something wrong");
    }
}


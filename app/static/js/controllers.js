'use strict';

/* Controllers */


function TestCtrl($scope) {
    $scope.test = ["yan","xing"];
}

function SizhenInfoListCtrl($scope, SizhenInfo) {
    $scope.sizheninfo_list = SizhenInfo.query();
}

function SizhenInfoDetailCtrl($scope, $routeParams, SizhenInfo) {
    $scope.sizheninfo = SizhenInfo.get({"patientID":$routeParams.patientID});
}

function AddInfoListCtrl($scope, AddInfo) {
    $scope.addinfo_list = AddInfo.query();
}

function AddInfoDetailCtrl($scope, $routeParams, AddInfo) {
    $scope.addinfo = AddInfo.get({"patientID":$routeParams.patientID});
}

function drugMgrCtrl($scope, $routeParams) {
    $scope.drug_list = [ {"name":"1", "code":"1", "unit":"1", "oname":"1", "classified":"1", "doctor":"1", "pinyin":"1", "wubi":"1", "state":"1"}]
} 

function wdiseaseMgrCtrl($scope, $routeParams) {
    $scope.wdisease_list = [ {"name":"2", "code":"2", "unit":"2", "oname":"2","classified":"2", "doctor":"2",  "state":"2"}]
}

function SizhenInfoConnectCtrl($scope, $routeParams, SizhenInfo) {
    $scope.addinfoID = $routeParams.addinfoID;
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


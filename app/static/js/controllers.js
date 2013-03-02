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

function DragLibCtrl($scope, $routeParams, AddInfo) {
    $scope.addinfo = AddInfo.get({"patientID":$routeParams.patientID});
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


$(function() {
    var app = angular.module('annotations', [
            'ngCookies',
            'restangular',
            'ui.router'
        ]).
        config([
            '$httpProvider',
            '$interpolateProvider',
            '$stateProvider',
            '$urlRouterProvider',
            function($httpProvider, $interpolateProvider, $stateProvider, $urlRouterProvider) {
                $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
                $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
                $httpProvider.defaults.xsrfCookieName = 'csrftoken';
                $interpolateProvider.startSymbol('[[');
                $interpolateProvider.endSymbol(']]');
                $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
                $urlRouterProvider.otherwise("/");
                $stateProvider
                    .state('index', {

                        url: "/",
                        templateUrl: "/static/annotations/html/index.html",
                        controller: "AnnController"
                    })
                    .state('edit', {

                        url: "/edit/{id:[0-9]*}",
                        templateUrl: "/annotation/form",
                        controller: "AnnFormController"
                    })
            }]);

    app.controller('AnnController', function($scope, $state, Restangular) {
        $scope.annotations = [];

        var baseAnnotations = Restangular.all('annotation');
        baseAnnotations.getList().then(function(data) {
            $scope.annotations = data;
        });

        $scope.go = function(item){
            $state.go('edit', { id: item.id });
        }
    });

    app.controller('AnnFormController', function($scope, $state, $stateParams, Restangular) {
        $scope.item = {
            start_time: 0,
            end_time: 0,
            text: ''
        };
        $scope.id = false;
        if ($stateParams.id){
            $scope.id = parseInt($stateParams.id);

            // load model
            Restangular.one('annotation', $scope.id).get().then(function(data){
                $scope.item = data;
            });
        }

        $scope.next = function(id){
            Restangular.oneUrl('test', '/annotation/'+id+'/next/').get().then(function(next){
                $state.go('edit', { id: next.id });
            }, function(){
                $state.go('index');
            });
        }

        $scope.prev = function(id){
            Restangular.oneUrl('test', '/annotation/'+id+'/prev/').get().then(function(prev){
                $state.go('edit', { id: prev.id });
            }, function(){
                $state.go('index');
            });
        }

        $scope.saveItem = function(){
            if ($scope.id) {
                $scope.item.put().then(function(){
                    $state.go('index');
                });
            } else {
                Restangular.all('annotation').customPOST($.param($scope.item), '', {}, {'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"}).then(function(data){
                    $state.go('index');
                });
            }
        }

    });

});

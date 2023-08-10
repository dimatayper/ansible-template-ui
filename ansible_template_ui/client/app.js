// !/usr/bin/env python
// -*- coding: utf-8 -*-
// Copyright 2017-2018 Matt Martz
// Copyright 2023 Dmitry Titov
// All Rights Reserved.
//
//    Licensed under the Apache License, Version 2.0 (the "License"); you may
//    not use this file except in compliance with the License. You may obtain
//    a copy of the License at
//
//         http://www.apache.org/licenses/LICENSE-2.0
//
//    Unless required by applicable law or agreed to in writing, software
//    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
//    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
//    License for the specific language governing permissions and limitations
//    under the License.

(function() {
    const ngApp = angular.module('ngApp', ['blockUI', 'ui.bootstrap']);

    ngApp.controller('mainController', [
        '$scope',
        '$http',
        '$sce',
        function($scope, $http, $sce) {
            $scope.variables = '';
            $scope.template = '';
            $scope.rendered = '';
            $scope.error = '';
            $scope.templateExample = '{{ foo }}';
            $scope.raw = false;

            $scope.sample = function() {
                $scope.variables = 'foo: bar';
                $scope.template = $scope.templateExample;
                $scope.raw = false;
                $scope.render();
            };

            $scope.render = function(tag = 'latest') {
                const template = $scope.raw ? `{{ ${$scope.template} }}` : $scope.template;
                $scope.rendered = '';
                $scope.error = '';
                
                $http.post('render', {
                    variables: $scope.variables,
                    template: template,
                    tag: tag,
                }).then(
                    function(response) {
                        console.log(response);
                        $scope.rendered = response.data.content;
                    },
                    function(response) {
                        console.log(response);
                        $scope.error = response.data.error;
                    }
                );
            };
        }
    ]);
})();

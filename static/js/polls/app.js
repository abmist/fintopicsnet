/**
 * Created by Aaron on 14/03/2016.
 */

var pollApp = angular.module('pollApp', []);

pollApp.config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
    $httpProvider.defaults.headers.common['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
});



pollApp.factory('pollFactory', function($http) {
    var pollUrl = '/threads/polls/';
    var votingUrl = '/threads/polls/vote/';

    pollFactory = {};

    pollFactory.getPoll = function(id) {
        return $http.get(pollUrl + id);
    };

    pollFactory.vote = function(poll, subject) {
        var data = {'poll': poll.id, 'subject': subject.id};

        return $http.post(votingUrl + poll.thread + '/', data); // remember to add the slash for django urls to work!
    };

    return pollFactory;
});




pollApp.controller('PollCtrl', function($scope, pollFactory) {
    $scope.poll = "";

    function setPoll(response) {
        $scope.poll = response.data;
    }

    function showError(response) {
        if(response.data.error == undefined) {           // Before !== undefined
            alert(response.data.error);
        }
    }

    function getPoll() {
        return pollFactory.getPoll(pollID);    // pollID - from our page variable made in our template
    }

    getPoll().then(setPoll);

    $scope.vote = function(poll, subject) {
        pollFactory.vote(poll, subject).then(getPoll).then(setPoll, showError);
    }
});




from rest_framework import serializers
from .models import Vote, PollSubject, Poll


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'poll', 'subject', 'user')


class PollSubjectSerializer(serializers.ModelSerializer):

    votes = VoteSerializer(many=True)
    total_votes_per_subject = serializers.SerializerMethodField()
    percentage_votes_per_subject = serializers.SerializerMethodField()


    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes_per_subject', 'percentage_votes_per_subject')

    def get_total_votes_per_subject(self, subject):
        return subject.votes.count()

    def get_percentage_votes_per_subject(self, subject):
        total_votes = subject.poll.votes.count()
        if total_votes:
            return int(( float(subject.votes.count()) / float(total_votes) )*100)
        else:
            return 0


class PollSerializer(serializers.ModelSerializer):

    subjects = PollSubjectSerializer(many=True)
    user_has_voted = serializers.SerializerMethodField()
    total_votes = serializers.SerializerMethodField()


    class Meta:
        model = Poll
        fields = ('id', 'thread', 'question', 'subjects', 'user_has_voted', 'total_votes')

    def get_user_has_voted(self, poll):
        has_voted = False
        request = self.context.get('request', None)

        if request:
            return False

        if not request.user.is_authenticated():
            return True


        vote = poll.votes.filter(user_id=request.user.id).first()

        if vote:
            has_voted = True

        return has_voted

    def get_total_votes(self, poll):
        return poll.votes.count()

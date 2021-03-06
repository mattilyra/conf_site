from django.test import TestCase

from symposion.conference.models import Conference, Section
from symposion.proposals.models import ProposalKind
from symposion.speakers.models import Speaker

from conf_site.proposals.models import Proposal


class ProposalTestCase(TestCase):
    def setUp(self):
        # Create base conference infrastructure that has to exist in
        # order to create a Proposal.
        conference = Conference(title="Conference")
        conference.save()
        section = Section(
            conference=conference, name="Section", slug="section")
        section.save()
        proposal_kind = ProposalKind(section=section, name="Kind", slug="kind")
        proposal_kind.save()
        speaker = Speaker(name="Paul Ryan")
        speaker.save()
        self.proposal = Proposal.objects.create(
            title="Title",
            description="Description",
            abstract="Abstract",
            kind=proposal_kind,
            speaker=speaker,
            audience_level=1,
        )

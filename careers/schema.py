import graphene
from graphene_django.types import DjangoObjectType

from .graphql_nodes import CustomNode

from . import models


class CareerPositionType(DjangoObjectType):
    class Meta:
        model = models.CareerPosition
        interfaces = (CustomNode, )


class Query(object):
    career_positions = graphene.List(CareerPositionType)

    def resolve_career_positions(self, info):
        return models.CareerPosition.objects.filter(is_published=True)

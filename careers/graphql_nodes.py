"""Custom nodes for GraphQL."""
from graphene import Node


class CustomNode(Node):  # pragma: nocover
    """
    A little hack to make sure that we can query objects by PK.

    By default, they can only be queried by special IDs, which seems to be a
    feature that is used by Relay, but not neccessary for Apollo.

    """
    class Meta:
        name = 'CustomNode'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def get_node_from_global_id(id, context, info, only_type=None):
        return info.return_type.graphene_type._meta.model.objects.get(id=id)

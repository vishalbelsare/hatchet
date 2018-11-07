##############################################################################
# Copyright (c) 2017-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Hatchet.
# Created by Abhinav Bhatele <bhatele@llnl.gov>.
# LLNL-CODE-741008. All rights reserved.
#
# For details, see: https://github.com/LLNL/hatchet
# Please also read the LICENSE file for the MIT License notice.
##############################################################################

from .external.printtree import trees_as_text
from .util.dot import trees_as_dot


class Graph:
    """ A possibly multi-rooted tree or graph from one input dataset.
    """

    def __init__(self, roots):
        if roots is not None:
            self.roots = roots

    def to_string(self, roots=None, dataframe=None,
                  metric='CPUTIME (usec) (I)', name='name', context='file',
                  rank=0, threshold=0.01, unicode=True, color=True):
        """ Print the graph with or without some metric attached to each
            node.
        """
        if roots is None:
            roots = self.roots

        result = trees_as_text(roots, dataframe, metric, name, context, rank,
                               threshold, unicode=unicode, color=color)

        return result

    def to_dot(self, roots=None, dataframe=None, metric='inc', name='name',
               rank=0, threshold=0.0):
        """ Write the graph in the graphviz dot format:
            https://www.graphviz.org/doc/info/lang.html
        """
        if roots is None:
            roots = self.roots

        result = trees_as_dot(roots, dataframe, metric, name, rank, threshold)

        return result

    def __str__(self):
        """ Returns a string representation of the graph.
        """
        return self.to_string()
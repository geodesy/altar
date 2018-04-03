# -*- python -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
#
# (c) 2013-2018 parasim inc
# (c) 2010-2018 california institute of technology
# all rights reserved
#

# support
import altar


# the simple application shell
class Application(altar.application, family="altar.shells.application"):
    """
    The base class for simple AlTar applications
    """


    # user configurable state
    job = altar.simulations.run()
    job.doc = "the job input parameters"


    # protocol obligations
    @altar.export
    def main(self, *args, **kwds):
        """
        The main entry point
        """
        # grab the job parameters
        job = self.job
        # initialize it
        job.initialize(app=self)
        # sample the posterior distribution
        return job.model.posterior(app=self)


    # pyre framework hooks
    # interactive session management
    def pyre_interactiveSessionContext(self, context):
        """
        Go interactive
        """
        # protect against bad context
        if context is None:
            # by initializing an empty one
            context = {}
        # add some symbols
        context["altar"] = altar # my package
        # and chain up
        return super().pyre_interactiveSessionContext(context=context)


# end of file

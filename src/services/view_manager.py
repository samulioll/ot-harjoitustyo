class ViewManager():
    """
    Keeps track of what view to show and handles the switching between views.
    """

    def __init__(self):
        self.running = True
        self.views = {}
        self.view = None
        self.profile = None
        self.start_view = None
        self.profiles = None

    def initialize_views(self, views, start_view):
        """ Initializes the list of views and sets the starting view. """
        self.views = views
        self.start_view = start_view
        self.view = self.views[start_view]

    def initialize_profiles(self, profiles):
        """ Initializes the profiles list. """
        self.profiles = profiles
        self.profile = None

    def event_handler(self, event):
        """ Passes the events to the current view to handle. """
        self.view.input_handler(event)

    def draw(self, surface):
        """ Passes the surface to the current view to draw on. """
        self.view.draw(surface)

    def update(self):
        """ Checks if the current view is done and initializes change if so. """
        if self.view.done:
            self.switch_view()

    def switch_view(self):
        """ Handles the switch from one view to another. """
        print("View changing to", self.view.next)
        self.start_view = self.view.next
        profile = self.view.closure()
        self.view = self.views[self.view.next]
        self.view.startup(profile)
        self.view.done = False
        if self.view == self.views["GAME"]:
            self.view.initiate_level()


class View():
    """ Baseline parent for all of the different views """

    def __init__(self):
        self.done = False
        self.profile = None

    def startup(self, active_profile):
        """ Loads the profile info from last view. """
        self.profile = active_profile

    def closure(self):
        """ Saves the profile infor for the next view. """
        self.done = False
        return self.profile
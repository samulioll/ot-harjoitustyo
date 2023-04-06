from data.components import profile

class ViewManager():

    def __init__(self):
        self.running = True
        self.views = {}
        self.view = None
        self.profile = None

    def initialize_views(self, views, start_view):
        """
        Initializes the different views and sets the starting view.
        """
        self.views = views
        self.start_view = start_view
        self.view = self.views[start_view]

    def initialize_profiles(self, profiles):
        """
        Initializes the profiles list.
        """
        self.profiles = profiles
        self.profile = None

    def event_handler(self, event):
        """
        Passes the events to the current view to handle.
        """
        self.view.input_handler(event)
            

    def draw(self, surface):
        self.view.draw(surface)

    def update(self):
        if self.view.done:
            self.switch_view()

    def switch_view(self):
        print("View changing to", self.view.next)
        previous, self.start_view = self.start_view, self.view.next
        profile = self.view.closure()
        self.view = self.views[self.view.next]
        self.view.startup(profile)
        self.view.done = False
        if self.view == self.views["GAME"]:
            self.view.initiate_level()



class _View():
    """
    Baseline for all of the different views.
    """
    def __init__(self):
        self.done = False
        self.profile = None
        
    def get_event(self, event):
        pass

    def update(self):
        pass

    def startup(self, active_profile):
        self.profile = active_profile
    
    def closure(self):
        self.done = False
        return self.profile
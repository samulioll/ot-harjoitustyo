class ViewManager():

    def __init__(self):
        self.running = True
        self.views = {}
        self.view = None

    def initialize_views(self, views, start_view):
        """
        Initializes the different views and sets the starting view.
        """
        self.views = views
        self.start_view = start_view
        self.view = self.views[start_view]


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
        self.view = self.views[self.view.next]



class _View():
    """
    Baseline for all of the different views.
    """
    def __init__(self):
        self.done = False
        
    def get_event(self, event):
        pass

    def update(self):
        pass
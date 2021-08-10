from gatenlp import Document, AnnotationSet, GateNlpPr, interact

@GateNlpPr
class MyAnnotator:
    def __init__(self):
        self.n_docs = 0
    def __call__(self, doc, **kwargs):
        self.n_docs += 1
        doc.annset().add(0,3,"SomeType")
        doc.features["docnr"] = self.n_docs
    def start(self, **kwargs):
        print("Processing starting, we got kwargs:", kwargs)
        self.n_docs = 0
    def finish(self, **kwargs):
        print("Processing finished, documents processed: ", self.n_docs)

if __name__ == "__main__":
    interact()

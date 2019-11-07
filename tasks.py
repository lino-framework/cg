from atelier.invlib import setup_from_tasks

cfg = dict()
# cfg.update(tolerate_sphinx_warnings=True)
cfg.update(blog_root='/home/luc/work/blog/')
cfg.update(languages=['en', 'de', 'fr'])
cfg.update(doc_trees=['docs'])
cfg.update(revision_control_system='git')
cfg.update(intersphinx_urls=dict(docs="http://community.lino-framework.org"))
ns = setup_from_tasks(globals(), **cfg)
# ns.configure(cfg)

(TeX-add-style-hook
 "acoustic"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "10pt" "conference" "compsocconf")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("amsmath" "cmex10")))
   (TeX-run-style-hooks
    "latex2e"
    "IEEEtran"
    "IEEEtran10"
    "amsmath"
    "tikz"
    "listings"
    "algorithm"
    "algorithmic"
    "subcaption"
    "etoolbox"
    "minted"
    "color"
    "verbatim"
    "caption"
    "mdframed"
    "stmaryrd"
    "amssymb"
    "multirow")
   (TeX-add-symbols
    '("FORALLP" ["argument"] 1)
    '("norm" 1)
    '("iseg" 1)
    "nset"
    "zset"
    "rset"
    "cset"
    "qset"
    "algorithmicdoinparallel")
   (LaTeX-add-labels
    "Introduction"
    "fig:digital"
    "Related"
    "Framework"
    "fig:gen"
    "fig:training"
    "Model"
    "fig:arch"
    "Orchestrator"
    "alg:Qwork"
    "alg:Qtask"
    "alg:Qparallel"
    "alg:Qworkflow"
    "fig:orch_ex"
    "fig:implementation_diagram"
    "fig:implementation_code"
    "Proof-of-concept"
    "subsec:extraction"
    "fig:integration"
    "table:dataset"
    "table:params"
    "fig:times_extraction"
    "subfig:coarse_glob"
    "subfig:coarse_ind"
    "fig:coarse-grained"
    "subfig:fine_glob"
    "subfig:fine_ind"
    "fig:fine-grained"
    "Conclusion")
   (LaTeX-add-environments
    "theorem"
    "lemma"
    "proposition"
    "corollary"
    "property"
    "definition"
    "remark"
    "assumption")
   (LaTeX-add-bibliographies))
 :latex)


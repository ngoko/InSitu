(TeX-add-style-hook "acoustic"
 (lambda ()
    (LaTeX-add-bibliographies)
    (LaTeX-add-environments
     "theorem"
     "lemma"
     "proposition"
     "corollary"
     "property"
     "definition"
     "remark"
     "assumption")
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
     "Conclusion")
    (TeX-add-symbols
     '("FORALLP" ["argument"] 1)
     '("norm" 1)
     "algorithmicdoinparallel")
    (TeX-run-style-hooks
     "mdframed"
     "caption"
     "verbatim"
     "color"
     "minted"
     "etoolbox"
     "subcaption"
     "algorithmic"
     "algorithm"
     "listings"
     "tikz"
     ""
     "amsmath"
     "cmex10"
     "latex2e"
     "IEEEtran10"
     "IEEEtran"
     "compsocconf"
     "conference"
     "10pt"
     "./Figures/Aggregation")))


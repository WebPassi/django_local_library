\definecolor{cqcqcq}{rgb}{0.75,0.75,0.75}
\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
\draw [color=cqcqcq,dash pattern=on 2pt off 2pt, xstep=1.0cm,ystep=1.0cm] (-5.33,-2.57) grid (5.29,5.53);
\draw[->,color=black] (-5.33,0) -- (5.29,0);
\foreach \x in {-5,-4,-3,-2,-1,1,2,3,4,5}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[color=black] (5,0.07) node [anchor=south west] { x};
\draw[->,color=black] (0,-2.57) -- (0,5.53);
\foreach \y in {-2,-1,1,2,3,4,5}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0.09,5.17) node [anchor=west] { y};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
\clip(-5.33,-2.57) rectangle (5.29,5.53);
\draw(-5,5.01) -- (-3.18,5.01);
\draw(-5,4.01) -- (-3.18,4.01);
\draw [domain=-5.33:5.29] plot(\x,{(--2--0.5*\x)/1});
\begin{scriptsize}
\fill [color=black] (-4,5.01) circle (1.5pt);
\draw[color=black] (-3.76,5.33) node {$m = 0.5$};
\fill [color=black] (-3.73,4.01) circle (1.5pt);
\draw[color=black] (-3.63,4.33) node {$c = 2$};
\end{scriptsize}
\end{tikzpicture}



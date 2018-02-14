% Intro Options
\ProvidesClass{main}[2014/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
	\PassOptionsToClass{\CurrentOption}{article}
}
\ProcessOptions\relax
\LoadClass[a4paper]{article}


%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------
%\documentclass[a4paper]{article}

\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,latexsym,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage[colorinlistoftodos]{todonotes}
\usepackage[T1]{fontenc} % Output font encoding for international characters
\usepackage{algorithmic,algorithm}
\usepackage{mathpazo} % Palatino font
\usepackage{cite}
\usepackage{titlesec}

% Packages needed?
\usepackage{fancyhdr}
\usepackage{a4wide}
\usepackage{url}
\usepackage{ifthen}

%----------------------------------------------------------------------------------------
%	COMMANDS
%----------------------------------------------------------------------------------------
% usefull Shortcuts
\newcommand{\ie}{{\it i.e.}}
\newcommand{\etal}{{\it et al.}}
\newcommand{\eg}{{\it e.g.}}

% Date command
\usepackage[absolute]{textpos}
\usepackage[UKenglish]{isodate}
\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\newcommand{\lastupdated}{\begin{textblock}{60}(155,5)
		\fontsize{8pt}{10pt}\selectfont 
		Last Updated on \today
\end{textblock}}

% Title Command
\usepackage[export]{adjustbox}
\newcommand{\titlesection}[1]{
	\begin{minipage}[t]{0.4\textwidth} 
		\begin{adjustbox}{valign=c}
			\centering
			\noindent\includegraphics[width=5cm]{#1}
		\end{adjustbox}
	\end{minipage}%\quad %for a bigger space between minipages
	\begin{minipage}[t]{0.6\textwidth} 
		\fontsize{15pt}{15pt}\selectfont
		Graz University of Technology \\
		\fontsize{11pt}{14pt}\selectfont
		\textbf{IAIK\\ Institute for Applied Information Processing and Communications} \\
		Inffeldgasse 16a \\
		A-8010 Graz
	\vspace{20pt}
	\end{minipage}
	%\noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}
}
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
\usepackage[T1]{fontenc} % Output font encoding for international characters
\usepackage[utf8]{inputenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{cite}
\usepackage{titlesec}
\usepackage{a4wide}
\usepackage{url}
\usepackage{spverbatim}
\usepackage{listings}
\usepackage{amsmath}

%\usepackage{float}
% Packages needed?
%\usepackage{algorithmic,algorithm}
%\usepackage{amsmath,latexsym,amssymb,amsfonts}
%\usepackage{mathpazo} % Palatino font
%\usepackage{fancyhdr}
%\usepackage{ifthen}
%\usepackage[colorinlistoftodos]{todonotes}

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
	\centering
	\begin{minipage}[t]{0.75\textwidth} 
		\fontsize{15pt}{15pt}\selectfont
		Graz University of Technology \\
		\fontsize{11pt}{14pt}\selectfont
		\textbf{IAIK\\ Institute for \\ Applied Information  Processing and Communications} \\
		Inffeldgasse 16a \\
		A-8010 Graz
	\end{minipage}%\quad %for a bigger space between minipages
	\begin{minipage}[t]{0.25\textwidth} 
		\begin{adjustbox}{valign=t}
			\includegraphics[scale=1]{#1}
		\end{adjustbox}
	\end{minipage}
	%\noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}
}

% Change Font Command 
% use either 
% ptm -> Times
% ppl -> Palatino
% pcr -> Courier
\usepackage{times}
\usepackage{palatino}
\usepackage{courier}
\newcommand{\ChangeFont}[1]{
\fontfamily{#1}\selectfont
}
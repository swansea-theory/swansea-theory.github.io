---
layout: post
title: "Theory Seminar Series"
date: 2024-10-21
---

The theory seminar tomorrow will be given by Eike on "Robust Decidability of Escape Problems for General Non-Linear Systems."  
  

**Abstract:**  
A wide range of problems from a diverse range of areas can be formulated as "escape problems": does a given point escape a set under the iteration of a function, or do all points in a given set escape the set under the function.  
  
The decidability of these problems is almost exclusively studied under the assumption that points, functions, and sets are specified exactly by a finite amount of data (e.g. rational or algebraic parameters). In this setting, positive results are largely limited to linear systems, since already very simple non-linear systems can have undecidable escape problems.  
  
When working with systems that involve real data, say, coming from scientific or engineering applications, the assumption that the system be known to infinite precision is arguably unrealistic. One should rather assume that the system is known only up to finite precision. In that case, the natural question becomes whether the system's behaviour -- escaping or not escaping -- is robust under all sufficiently small perturbations. On the one hand, this requires us in some sense to do more than to decide the problem for a single given point at a time. On the other hand, there appears to be little value in determining the status of problem instances that lie on a "decision boundary", i.e. instances that are not robust under small perturbation. The latter point is interesting in light of the aforementioned undecidability results in the discrete-data setting, which appear to rely on the existence of very difficult non-robust instances.  
  
The aim of this talk is to demonstrate by means of a case study that computable analysis constitutes an excellent framework for the discussion of robust decidability questions, such as the above. I will study to escape problems for very general non-linear systems and show at least in one case that the problem becomes as close to decidable as one can hope it to be in this setting. The Point Escape Problem is to decide for a given continuous map f, a given closed set A, and a given point x in A whether x escapes A under iteration of f. The Set Escape Problem is to decide for a given continuous map f and a given compact set K whether all points of K escape K under iteration of f. I will give a complete algorithm for the Point Escape Problem and a potentially not complete algorithm for the Set Escape Problem. I will show that both algorithms terminate generically, and discuss some concrete examples of termination problems.


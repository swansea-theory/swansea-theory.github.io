---
layout: post
title: "Mukesh on Formally Verified Verifiable Group Generators "
date: 2025-06-10
seminar: true
feature: https://ik.imagekit.io/s1sp3stox/tr:h-200,w-200,fo-none/staff/mukesh.tiwari/Tiwari_Mukesh_Profile_Comp-Sci.jpg
---

Mukesh will give a talk on Formally Verified Verifiable Group Generators as a part of our seminar series this Thursday.

  

**Abstract:**

Electronic voting (e-voting) requires a trusted setup to initiate an election process. This setup must be transparent to maintain the integrity of the election. A crucial aspect of this trusted setup involves generating group generators for a finite cyclic group, which are then used in cryptographic algorithms deployed within the voting system. Although computing group generators is generally not considered a difficult problem, election verifiability – where every step can be ascertained by independent third parties – excludes many of them, as they fail to provide verifiable evidence of correctness. In this work, we present a formally verified implementation of the group generator algorithm A.2.3 and the group generator verification algorithm A.2.4, specified in the National Institute of Standards and Technology (NIST), FIPS 186-4, in the Coq theorem prover. These two algorithms are highly sought-after methods to compute and verify group generator(s), respectively, because their outcomes can be established independently by third parties. Our formalisation captures all the requirements specified in algorithms A.2.3 and A.2.4 using the expressive type system of the Rocq theorem prover. We evaluate the group generator algorithm within the Rocq theorem prover itself to produce group generators, thereby only trusting the Rocq and its evaluation mechanism. In fact, our implementation is so efficient that it can compute the group generators used in real-world democratic elections in 30 min on a M3 laptop. The source code of this formalisation is available at GitHub [1].

  

[1] https://github.com/mukeshtiwari/Formally_Verified_Verifiable_Group_Generator/


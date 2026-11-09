#!/usr/bin/env bash

read -p "What is the date? (YYYY-MM-DD) " DATE
read -p "What is the name? (Firstname Surname) " NAME
read -p "What is the title? " TITLE
read -p "What is the abstract? " ABSTRACT

FIRSTNAME=${NAME%% *}
FILE="_posts/${DATE}-${FIRSTNAME}.md"

touch $FILE
cat > $FILE <<EOF
---
layout: post
title: "${NAME}: ${TITLE}"
date: ${DATE}
seminar: true
---

The speaker for next week's theory seminar will be ${NAME} (see title and abstract below). We will meet next Tuesday at 2pm in the theory lab.

**Title**

${TITLE}

**Abstract**

${ABSTRACT}
EOF

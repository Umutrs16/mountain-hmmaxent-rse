#!/usr/bin/env Rscript
# Minimal maxnet wrapper. Input CSV must contain a binary `presence` column and predictor columns.
suppressPackageStartupMessages({library(maxnet); library(data.table)})
args <- commandArgs(trailingOnly=TRUE)
if (length(args) < 2) stop("Usage: fit_maxnet.R input.csv output.csv [predictor1 predictor2 ...]")
infile <- args[[1]]; outfile <- args[[2]]
dt <- fread(infile)
preds <- if (length(args) > 2) args[3:length(args)] else setdiff(names(dt), c("presence","row_id"))
x <- as.data.frame(dt[, ..preds]); y <- dt$presence
m <- maxnet(y, x, f=maxnet.formula(y, x, classes="lqh"), regmult=1.5)
dt[, prediction := predict(m, x, type="cloglog")]
fwrite(dt[, .(row_id=if ("row_id" %in% names(dt)) row_id else .I, prediction)], outfile)

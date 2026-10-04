# Databricks notebook source
customer_df = spark.sql("SELECT * FROM finguard.bronze.customers")
display(customer_df)
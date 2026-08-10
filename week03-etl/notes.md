# Week 03 ETL Notes

## ETL vs ELT

ETL stands for Extract, Transform, Load. In this model, data is read from a source, cleaned or reshaped, and then loaded into a destination system. ELT is a related pattern where data is first loaded into a storage system and transformed later, often inside the warehouse or lakehouse. ETL is commonly used when transformations are needed before storage, while ELT is popular in modern analytics platforms because it keeps raw data available for flexible downstream use.

## pathlib

The pathlib module provides an object-oriented way to work with file paths in Python. Instead of manually handling strings, developers can use Path objects to create, inspect, and join file paths safely. This makes code clearer and less error-prone, especially when working across operating systems.

## Configuration Management

Configuration management helps keep pipeline behavior consistent and easier to change. Settings such as input paths, output locations, and environment-specific values should be managed carefully instead of being hard-coded in many places. In production systems, configuration is often separated from application logic so it can be updated without changing the code.

## CSV Extraction

CSV extraction is one of the simplest forms of data ingestion. A pipeline can read rows from a CSV file using the csv module and turn them into a list of dictionaries. Extraction should remain focused on reading data from the source and should not include validation, cleaning, or business logic. That separation keeps the pipeline easier to understand and maintain.

## Logging Basics

Logging is used to record useful information while a pipeline runs. Unlike print statements, logging supports different levels such as INFO, WARNING, and ERROR, and it is better suited for production environments. Good logging helps operators monitor pipeline execution, diagnose failures, and audit important events without cluttering the code with ad-hoc output.

## Why Modular Design Matters

Modular design breaks a pipeline into small, focused functions and files. This makes it easier to test, reuse, and maintain code. When each stage of the pipeline has a clear responsibility, changes are less risky and new features can be added more cleanly. A modular ETL pipeline is also easier for teams to collaborate on because responsibilities are well defined.

## CSV and JSON

CSV and JSON are common data interchange formats. CSV is a row-based format that is easy to inspect and read with Python's csv module. JSON is a structured format that can represent nested objects and arrays and is commonly used in APIs and configuration files. Choosing the right format depends on source system requirements and downstream processing needs.

## Generic Functions and Wrapper Functions

Generic functions are reusable helpers that solve a general problem, such as reading any CSV or JSON file. Wrapper functions sit on top of those helpers and provide a more specific interface for a particular business use case. For example, a generic extract_csv function can be wrapped by a function that extracts employee data from a known file path. This pattern reduces duplication and keeps code easier to extend.

## Configuration and Error Handling

Configuration values such as input file paths and output directories should be stored in one place so they are easy to update. Error handling should make failures understandable. Raising clear exceptions such as FileNotFoundError, RuntimeError, or ValueError helps developers quickly identify issues without losing the original cause.

## Clean Architecture in ETL

A clean architecture keeps the pipeline organized by responsibility. The Extract layer collects data from sources, the Transform layer cleans and reshapes it, and the Load layer writes it to its destination. This separation makes it easier to test each stage independently and to swap out components when requirements change.

> The Extract layer is responsible only for retrieving data. It should not clean, validate, or transform records. Keeping extraction focused on data retrieval makes the pipeline easier to maintain and extend.

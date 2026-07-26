# Design Decisions

## Why use dataclasses for context?

The PipelineContext dataclass allows each filter to receive a single, explicit object containing all state. This avoids hidden shared variables and keeps the interfaces simple and readable.

## Why use a Pipe & Filter design?

The project uses Pipe & Filter because it aligns naturally with the flow of a machine learning pipeline: data enters, it is validated, cleaned, engineered, split, modeled, evaluated, and reported. Each filter is easy to replace and test independently.

## Why use a random forest classifier?

A random forest classifier offers strong baseline performance while also providing feature importances, which lets the project generate an additional artifact for portfolio value.

## Why focus on quality over model complexity?

The goal is to demonstrate engineering discipline. A simple but well-structured pipeline is more valuable for a portfolio than a complex model implemented without rigor.

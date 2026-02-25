# Structure

## Folder structure

```
docker/
    docker-compose.yml
    initdb/
        001_schema.sql

notebooks/
    00_sandbox.ipynb
    01_extract.ipynb
    02_load.ipynb
    00_transform.ipynb

scripts/
    main_scripts.py

tests/
    main_tests.py

src/
    market_extractor/
    __init__.py
    config.py
    logging.py

    db/
        __init__.py
        engine.py
        migrations.py
        models.py

    extract/
        __init__.py
        providers/
            yf_provider.py

    load/
        __init__.py

    utils/
        __init__.py
        time_utils.py
        files_utils.py
        data_utils.py


    pipelines/
        __init__.py

```

## Database Schemas

## Wireframe
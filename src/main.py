from .rag_engine import nl_to_sql, run_sql, format_results

def main():
    print("\nEmployee RAG Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ").strip()

        if query.lower() in ("exit", "quit"):
            break

        sql = nl_to_sql(query)
        print("\nGenerated SQL:\n", sql)

        result = run_sql(sql)
        print("\nResult:\n", format_results(result), "\n")


if __name__ == "__main__":
    main()

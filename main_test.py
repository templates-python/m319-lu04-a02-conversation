import main

def test_main(monkeypatch, capsys):
    inputs = iter(['I am doing well!', 'I love programming!'])
    prompts = []

    def mock_input(prompt):
        prompts.append(prompt)
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    main.main()
    captured = capsys.readouterr()

    # Check the prompts
    assert prompts == ['Greetings! How are you doing?', 'Oh, how interesting. Tell me more!']

    # Check the printed output
    assert captured.out == 'Thanks for sharing!\n'
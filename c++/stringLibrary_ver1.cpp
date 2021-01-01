#include<iostream>

class string {
	char* str = 0;
	int len = 0;
public:
	string(char c, int n); // 문자 c 가 n 개 있는 문자열로 정의
	string(const char* s);
	string(const string& s);
	~string();
	void add_string(const string& s); // str 뒤에 s 를 붙인다.
	void copy_string(const string& s); // str 에 s 를 복사한다.
	int strlen(); // 문자열 길이 리턴
	int strlen(const char* s);
	char* get_str();
};
string::string(char c, int n)
{
	if ((this->str = (char*)malloc(sizeof(char) * (n + 1))) != NULL)
	{
		char* _start_ptr = this->str;
		int _len_count = 0;
		while (n)
		{
			*_start_ptr = c;
			_len_count++, n--, _start_ptr++;
		}
		*_start_ptr = '\0';
		this->len = _len_count;
	}
	else
		this->len = 0;

}
string::string(const char* s)
{
	this->len = strlen(s);
	if ((this->str = (char*)malloc(sizeof(char) * (this->len + 1))) != NULL)
	{
		char* _start_str = this->str;
		while (*s)
		{
			*_start_str++ = *s++;
		}
		*_start_str = '\0';
	}

}

string::string(const string& s)
{
	this->copy_string(s);
}

string::~string()
{
	if (this->str != NULL)
	{
		free(this->str);
	}
}

int string::strlen(const char* s)
{
	ptrdiff_t index = 0;
	while (*s)
	{
		index++, s++;
	}
	return index;
}

int string::strlen()
{
	return this->len;
}

void string::add_string(const string& s)
{
	int _main_len = this->len;
	this->len += s.len;

	if (this->str != NULL)
	{
		if ((this->str = (char*)realloc(this->str, this->len + 1)) != NULL)
		{
			char* _sec_ptr = this->str + _main_len;
			char* _sec_str = s.str;
			while (*_sec_str)
			{
				*_sec_ptr++ = *_sec_str++;
			}
			*_sec_ptr = '\0';
		}
	}
}
void string::copy_string(const string& s)
{
	this->len = this->strlen(s.str);
	if (this->str != NULL)
	{
		if ((this->str = (char*)realloc(this->str, this->len + 1)) != NULL)
		{
			char* _start_main_ptr = this->str;
			char* _start_sec_ptr = s.str;
			while (*_start_sec_ptr)
			{
				*_start_main_ptr++ = *_start_sec_ptr++;
			}
			*_start_main_ptr = '\0';
		}
	}

}

char* string::get_str()
{
	return this->str;
}

int main()
{
	string a("oh");
	a.add_string(string(" good"));
	std::cout << a.get_str()<<'\n';

	a.copy_string(string("wow"));
	std::cout << a.get_str()<<'\n';
}

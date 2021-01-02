#include<iostream>
#include<chrono>

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
private:
	inline void chr_unit_processing(char* const start_ptr, const char* s);
	inline void int_unit_processing(char* const start_ptr, const char* s);
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
		int_unit_processing(this->str,s);
	}

}
inline void string::chr_unit_processing(char* const start_ptr,const char* s)
{
	char* _start_ptr = start_ptr;
	while (*s)
	{
		*_start_ptr++ = *s++;
	}
	*_start_ptr = '\0';
}
inline void string::int_unit_processing(char* const start_ptr, const char* s)
{
	int* _start_int_ptr = (int*)start_ptr;
	int* _sec_int_ptr = (int*)s;
	int strlen = this->len;

	while (strlen>4)
	{
		*_start_int_ptr++ = *_sec_int_ptr++;
		strlen -= 4;
	}

	chr_unit_processing((char*)_start_int_ptr, (char*)_sec_int_ptr);
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
			char* _main_ptr = this->str + _main_len;
			char* _sec_ptr = s.str;
			chr_unit_processing(_main_ptr, _sec_ptr);
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
	std::chrono::system_clock::time_point start = std::chrono::system_clock::now();
	string a("goooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood");
	std::cout << a.get_str()<<'\n';
	std::chrono::duration<double> sec = std::chrono::system_clock::now() - start;
	std::cout << "Test() 함수를 수행하는 걸린 시간(초) : " << sec.count() << " seconds" << std::endl;
}

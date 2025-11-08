<link rel="stylesheet" href="../assets/css/RC-stylesheet.css" />

# A05:2025 인젝션 (Injection) 

## 배경 (Background). 

인젝션은 순위에서 #3에서 #5로 두 단계 하락했으며, A04:2025-암호화 실패(Cryptographic Failures) 및 A06:2025-불안전한 설계(Insecure Design)에 비해 상대적 위치를 유지했습니다. 인젝션은 어떤 형태의 인젝션에 대해 테스트된 애플리케이션의 100%로 가장 많이 테스트되는 카테고리 중 하나입니다. 이 카테고리의 37개 CWE로 모든 카테고리 중 가장 많은 CVE를 가지고 있었습니다. 인젝션은 30k개 이상의 CVE를 가진 크로스 사이트 스크립팅(Cross-site Scripting, 높은 빈도/낮은 영향)과 14k개 이상의 CVE를 가진 SQL 인젝션(SQL Injection, 낮은 빈도/높은 영향)을 포함합니다. CWE-79 웹 페이지 생성 중 입력의 부적절한 중화('크로스 사이트 스크립팅', Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))에 대해 보고된 대량의 CVE는 이 카테고리의 평균 가중 영향을 낮춥니다. 


## 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>37
   </td>
   <td>13.77%
   </td>
   <td>3.08%
   </td>
   <td>100.00%
   </td>
   <td>42.93%
   </td>
   <td>7.15
   </td>
   <td>4.32
   </td>
   <td>1,404,249
   </td>
   <td>62,445
   </td>
  </tr>
</table>



## 설명 (Description). 

인젝션 취약점은 공격자가 프로그램의 입력 필드에 악의적인 코드나 명령(SQL 또는 셸 코드와 같은)을 삽입하여 시스템이 코드나 명령을 시스템의 일부인 것처럼 실행하도록 속일 수 있는 시스템 결함입니다. 이것은 정말 심각한 결과로 이어질 수 있습니다. 

애플리케이션은 다음 경우 공격에 취약합니다:

* 사용자가 제공한 데이터가 애플리케이션에 의해 검증, 필터링 또는 정제되지 않는 경우.
* 컨텍스트 인식 이스케이프 없이 동적 쿼리 또는 비매개변수화 호출이 인터프리터에서 직접 사용되는 경우.
* 정제되지 않은 데이터가 객체 관계 매핑(Object-Relational Mapping, ORM) 검색 매개변수 내에서 사용되어 추가적인 민감한 레코드를 추출하는 경우.
* 잠재적으로 적대적인 데이터가 직접 사용되거나 연결되는 경우. SQL 또는 명령에는 동적 쿼리, 명령 또는 저장 프로시저에서 구조와 악의적인 데이터가 포함됩니다.

더 일반적인 인젝션 중 일부는 SQL, NoSQL, OS 명령, 객체 관계 매핑(ORM), LDAP, 표현 언어(Expression Language, EL) 또는 객체 그래프 탐색 라이브러리(Object Graph Navigation Library, OGNL) 인젝션입니다. 개념은 모든 인터프리터에서 동일합니다. 탐지는 소스 코드 검토와 모든 매개변수, 헤더, URL, 쿠키, JSON, SOAP 및 XML 데이터 입력의 자동화된 테스트(퍼징 포함)를 결합하여 가장 잘 달성됩니다. CI/CD 파이프라인에 정적(SAST), 동적(DAST) 및 대화형(IAST) 애플리케이션 보안 테스트 도구를 추가하면 프로덕션 배포 전에 인젝션 결함을 식별하는 데 도움이 될 수 있습니다.

인젝션 취약점의 관련 클래스가 LLM에서 일반적이 되었습니다. 이것들은 [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)에서 별도로 논의되며, 특히 [LLM01:2025 프롬프트 인젝션 (LLM01:2025 Prompt Injection)](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)에서 그렇습니다.


## 예방 방법 (How to prevent). 

인젝션을 방지하는 최선의 수단은 데이터를 명령 및 쿼리와 분리하는 것을 요구합니다:

* 선호되는 옵션은 인터프리터를 전혀 사용하지 않고 매개변수화된 인터페이스를 제공하거나 객체 관계 매핑 도구(Object Relational Mapping Tools, ORM)로 마이그레이션하는 안전한 API를 사용하는 것입니다. 
**참고:** 매개변수화되었더라도, 저장 프로시저는 PL/SQL 또는 T-SQL이 쿼리와 데이터를 연결하거나 EXECUTE IMMEDIATE 또는 exec()로 적대적인 데이터를 실행하는 경우 여전히 SQL 인젝션을 도입할 수 있습니다.

데이터를 명령에서 분리할 수 없는 경우, 다음 기술을 사용하여 위협을 줄일 수 있습니다. 

* 긍정적 서버 측 입력 검증을 사용하세요. 이것은 많은 애플리케이션이 특수 문자를 요구하기 때문에 완전한 방어가 아닙니다. 예: 텍스트 영역 또는 모바일 애플리케이션용 API.
* 모든 잔여 동적 쿼리에 대해 해당 인터프리터에 대한 특정 이스케이프 구문을 사용하여 특수 문자를 이스케이프하세요. 
**참고:** 테이블 이름, 열 이름 등의 SQL 구조는 이스케이프할 수 없으므로 사용자가 제공한 구조 이름은 위험합니다. 이것은 보고서 작성 소프트웨어에서 일반적인 문제입니다.

**경고** 이러한 기술은 복잡한 문자열을 구문 분석하고 이스케이프하는 것을 포함하므로 오류가 발생하기 쉽고 기본 시스템의 사소한 변경에 직면하여 견고하지 않습니다. 

## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 애플리케이션이 계정 정보에 액세스하는 다음 취약한 SQL 호출 구축에서 신뢰할 수 없는 데이터를 사용합니다:

```
String query = "SELECT \* FROM accounts WHERE custID='" + request.getParameter("id") + "'";
```


**시나리오 #2:** 마찬가지로, 애플리케이션의 프레임워크에 대한 맹목적인 신뢰는 여전히 취약한 쿼리로 이어질 수 있습니다(예: Hibernate 쿼리 언어(Hibernate Query Language, HQL)):

```
Query HQLQuery = session.createQuery("FROM accounts WHERE custID='" + request.getParameter("id") + "'");
```

두 경우 모두, 공격자는 브라우저에서 'id' 매개변수 값을 수정하여 다음을 보냅니다: ' UNION SLEEP(10);--. 예를 들어:

```
http://example.com/app/accountView?id=' UNION SELECT SLEEP(10);--
```

이것은 두 쿼리의 의미를 변경하여 accounts 테이블의 모든 레코드를 반환합니다. 더 위험한 공격은 데이터를 수정하거나 삭제하거나 저장 프로시저를 호출할 수도 있습니다.

## 참고 자료 (References). 

* [OWASP 사전 대응 제어: 보안 데이터베이스 액세스 (OWASP Proactive Controls: Secure Database Access)](https://owasp.org/www-project-proactive-controls/v3/en/c3-secure-database)
* [OWASP ASVS: V5 입력 검증 및 인코딩 (OWASP ASVS: V5 Input Validation and Encoding)](https://owasp.org/www-project-application-security-verification-standard)
* [OWASP 테스트 가이드: SQL 인젝션,](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection) [명령 인젝션](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection), 및 [ORM 인젝션](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.7-Testing_for_ORM_Injection)
* [OWASP 치트 시트: 인젝션 방지 (OWASP Cheat Sheet: Injection Prevention)](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
* [OWASP 치트 시트: SQL 인젝션 방지 (OWASP Cheat Sheet: SQL Injection Prevention)](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
* [OWASP 치트 시트: Java의 인젝션 방지 (OWASP Cheat Sheet: Injection Prevention in Java)](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet_in_Java.html)
* [OWASP 치트 시트: 쿼리 매개변수화 (OWASP Cheat Sheet: Query Parameterization)](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)
* [OWASP 웹 애플리케이션에 대한 자동화된 위협 – OAT-014](https://owasp.org/www-project-automated-threats-to-web-applications/)
* [PortSwigger: 서버 측 템플릿 인젝션 (PortSwigger: Server-side template injection)](https://portswigger.net/kb/issues/00101080_serversidetemplateinjection)
* [Awesome Fuzzing: 퍼징 리소스 목록](https://github.com/secfigo/Awesome-Fuzzing) 


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-20 부적절한 입력 검증 (Improper Input Validation)](https://cwe.mitre.org/data/definitions/20.html)

* [CWE-74 다운스트림 구성 요소에서 사용하는 출력의 특수 요소 부적절한 중화 ('인젝션', Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection'))](https://cwe.mitre.org/data/definitions/74.html)

* [CWE-76 동등한 특수 요소의 부적절한 중화 (Improper Neutralization of Equivalent Special Elements)](https://cwe.mitre.org/data/definitions/76.html)

* [CWE-77 명령에서 사용되는 특수 요소의 부적절한 중화 ('명령 인젝션', Improper Neutralization of Special Elements used in a Command ('Command Injection'))](https://cwe.mitre.org/data/definitions/77.html)

* [CWE-78 OS 명령에서 사용되는 특수 요소의 부적절한 중화 ('OS 명령 인젝션', Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection'))](https://cwe.mitre.org/data/definitions/78.html)

* [CWE-79 웹 페이지 생성 중 입력의 부적절한 중화 ('크로스 사이트 스크립팅', Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'))](https://cwe.mitre.org/data/definitions/79.html)

* [CWE-80 웹 페이지에서 스크립트 관련 HTML 태그의 부적절한 중화 (기본 XSS, Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS))](https://cwe.mitre.org/data/definitions/80.html)

* [CWE-83 웹 페이지의 속성에서 스크립트의 부적절한 중화 (Improper Neutralization of Script in Attributes in a Web Page)](https://cwe.mitre.org/data/definitions/83.html)

* [CWE-86 웹 페이지의 식별자에서 잘못된 문자의 부적절한 중화 (Improper Neutralization of Invalid Characters in Identifiers in Web Pages)](https://cwe.mitre.org/data/definitions/86.html)

* [CWE-88 명령에서 인수 구분 기호의 부적절한 중화 ('인수 인젝션', Improper Neutralization of Argument Delimiters in a Command ('Argument Injection'))](https://cwe.mitre.org/data/definitions/88.html)

* [CWE-89 SQL 명령에서 사용되는 특수 요소의 부적절한 중화 ('SQL 인젝션', Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'))](https://cwe.mitre.org/data/definitions/89.html)

* [CWE-90 LDAP 쿼리에서 사용되는 특수 요소의 부적절한 중화 ('LDAP 인젝션', Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection'))](https://cwe.mitre.org/data/definitions/90.html)

* [CWE-91 XML 인젝션 (일명 블라인드 XPath 인젝션, XML Injection (aka Blind XPath Injection))](https://cwe.mitre.org/data/definitions/91.html)

* [CWE-93 CRLF 시퀀스의 부적절한 중화 ('CRLF 인젝션', Improper Neutralization of CRLF Sequences ('CRLF Injection'))](https://cwe.mitre.org/data/definitions/93.html)

* [CWE-94 코드 생성의 부적절한 제어 ('코드 인젝션', Improper Control of Generation of Code ('Code Injection'))](https://cwe.mitre.org/data/definitions/94.html)

* [CWE-95 동적으로 평가되는 코드에서 지시문의 부적절한 중화 ('Eval 인젝션', Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection'))](https://cwe.mitre.org/data/definitions/95.html)

* [CWE-96 정적으로 저장된 코드에서 지시문의 부적절한 중화 ('정적 코드 인젝션', Improper Neutralization of Directives in Statically Saved Code ('Static Code Injection'))](https://cwe.mitre.org/data/definitions/96.html)

* [CWE-97 웹 페이지 내 서버 측 포함(SSI)의 부적절한 중화 (Improper Neutralization of Server-Side Includes (SSI) Within a Web Page)](https://cwe.mitre.org/data/definitions/97.html)

* [CWE-98 PHP 프로그램에서 Include/Require 문에 대한 파일명의 부적절한 제어 ('PHP 원격 파일 포함', Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion'))](https://cwe.mitre.org/data/definitions/98.html)

* [CWE-99 리소스 식별자의 부적절한 제어 ('리소스 인젝션', Improper Control of Resource Identifiers ('Resource Injection'))](https://cwe.mitre.org/data/definitions/99.html)

* [CWE-103 Struts: 불완전한 validate() 메서드 정의 (Struts: Incomplete validate() Method Definition)](https://cwe.mitre.org/data/definitions/103.html)

* [CWE-104 Struts: Form Bean이 검증 클래스를 확장하지 않음 (Struts: Form Bean Does Not Extend Validation Class)](https://cwe.mitre.org/data/definitions/104.html)

* [CWE-112 XML 검증 누락 (Missing XML Validation)](https://cwe.mitre.org/data/definitions/112.html)

* [CWE-113 HTTP 헤더에서 CRLF 시퀀스의 부적절한 중화 ('HTTP 응답 분할', Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting'))](https://cwe.mitre.org/data/definitions/113.html)

* [CWE-114 프로세스 제어 (Process Control)](https://cwe.mitre.org/data/definitions/114.html)

* [CWE-115 출력의 잘못된 해석 (Misinterpretation of Output)](https://cwe.mitre.org/data/definitions/115.html)

* [CWE-116 출력의 부적절한 인코딩 또는 이스케이프 (Improper Encoding or Escaping of Output)](https://cwe.mitre.org/data/definitions/116.html)

* [CWE-129 배열 인덱스의 부적절한 검증 (Improper Validation of Array Index)](https://cwe.mitre.org/data/definitions/129.html)

* [CWE-159 특수 요소의 잘못된 사용에 대한 부적절한 처리 (Improper Handling of Invalid Use of Special Elements)](https://cwe.mitre.org/data/definitions/159.html)

* [CWE-470 클래스 또는 코드를 선택하기 위해 외부 제어 입력 사용 ('불안전한 리플렉션', Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection'))](https://cwe.mitre.org/data/definitions/470.html)

* [CWE-493 Final 수정자가 없는 중요한 공개 변수 (Critical Public Variable Without Final Modifier)](https://cwe.mitre.org/data/definitions/493.html)

* [CWE-500 Final로 표시되지 않은 공개 정적 필드 (Public Static Field Not Marked Final)](https://cwe.mitre.org/data/definitions/500.html)

* [CWE-564 SQL 인젝션: Hibernate (SQL Injection: Hibernate)](https://cwe.mitre.org/data/definitions/564.html)

* [CWE-610 다른 영역의 리소스에 대한 외부 제어 참조 (Externally Controlled Reference to a Resource in Another Sphere)](https://cwe.mitre.org/data/definitions/610.html)

* [CWE-643 XPath 표현식 내 데이터의 부적절한 중화 ('XPath 인젝션', Improper Neutralization of Data within XPath Expressions ('XPath Injection'))](https://cwe.mitre.org/data/definitions/643.html)

* [CWE-644 스크립팅 구문에 대한 HTTP 헤더의 부적절한 중화 (Improper Neutralization of HTTP Headers for Scripting Syntax)](https://cwe.mitre.org/data/definitions/644.html)

* [CWE-917 표현 언어 문에서 사용되는 특수 요소의 부적절한 중화 ('표현 언어 인젝션', Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection'))](https://cwe.mitre.org/data/definitions/917.html)

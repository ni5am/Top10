<link rel="stylesheet" href="../assets/css/RC-stylesheet.css" />

# A07:2025 인증 실패 (Authentication Failures)


## 배경 (Background). 

인증 실패는 이 카테고리의 36개 CWE를 더 정확하게 반영하기 위해 약간의 이름 변경과 함께 #7 위치를 유지합니다. 표준화된 프레임워크의 이점에도 불구하고, 이 카테고리는 2021년부터 #7 순위를 유지했습니다. 주목할 만한 CWE에는 *CWE-259 하드코딩된 암호 사용 (Use of Hard-coded Password)*, *CWE-297: 호스트 불일치가 있는 인증서의 부적절한 검증 (Improper Validation of Certificate with Host Mismatch)*, *CWE-287: 부적절한 인증 (Improper Authentication)*, *CWE-384: 세션 고정 (Session Fixation)*, *CWE-798 하드코딩된 자격 증명 사용 (Use of Hard-coded Credentials)*이 포함됩니다.


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
   <td>36
   </td>
   <td>15.80%
   </td>
   <td>2.92%
   </td>
   <td>100.00%
   </td>
   <td>37.14%
   </td>
   <td>7.69
   </td>
   <td>4.44
   </td>
   <td>1,120,673
   </td>
   <td>7,147
   </td>
  </tr>
</table>



## 설명 (Description). 

공격자가 시스템이 잘못되었거나 잘못된 사용자를 합법적인 것으로 인식하도록 속일 수 있을 때 이 취약점이 존재합니다. 애플리케이션이 다음인 경우 인증 약점이 있을 수 있습니다:

* 공격자가 유효한 사용자 이름과 암호의 침해 목록을 가지고 있는 자격 증명 스터핑(credential stuffing)과 같은 자동화된 공격을 허용하는 경우. 최근에 이 유형의 공격은 하이브리드 암호 공격 자격 증명 스터핑(암호 스프레이 공격이라고도 함)을 포함하도록 확장되었습니다. 여기서 공격자는 유출된 자격 증명의 변형이나 증분을 사용하여 액세스를 얻습니다. 예: Password1!, Password2!, Password3! 등을 시도합니다.

* 빠르게 차단되지 않는 무차별 대입(brute force) 또는 기타 자동화된 스크립트 공격을 허용하는 경우.

* "Password1" 또는 "admin" 사용자 이름과 "admin" 암호와 같은 기본, 약하거나 잘 알려진 암호를 허용하는 경우.

* 이미 알려진 침해된 자격 증명으로 새 계정을 만들 수 있도록 허용하는 경우.

* "지식 기반 답변"과 같이 안전하게 만들 수 없는 약하거나 비효과적인 자격 증명 복구 및 암호 찾기 프로세스 사용을 허용하는 경우.

* 평문, 암호화 또는 약하게 해시된 암호 데이터 저장소를 사용하는 경우(참조[ A02:2021-암호화 실패 (Cryptographic Failures)](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)).

* 다중 인증(multi-factor authentication)이 누락되었거나 비효과적인 경우.

* 다중 인증을 사용할 수 없는 경우 약하거나 비효과적인 대체 방법 사용을 허용하는 경우. 

* 세션 식별자가 URL, 숨겨진 필드 또는 클라이언트가 액세스할 수 있는 다른 불안전한 위치에 노출되는 경우.

* 성공적인 로그인 후 동일한 세션 식별자를 재사용하는 경우.

* 로그아웃 또는 비활성 기간 동안 사용자 세션 또는 인증 토큰(주로 단일 사인온(Single Sign-On, SSO) 토큰)을 올바르게 무효화하지 않는 경우.


## 예방 방법 (How to prevent). 

* 가능한 경우, 자동화된 자격 증명 스터핑, 무차별 대입 및 도난당한 자격 증명 재사용 공격을 방지하기 위해 다중 인증 사용을 구현하고 강제하세요.

* 가능한 경우, 사용자가 더 나은 선택을 할 수 있도록 암호 관리자 사용을 권장하고 활성화하세요.

* 특히 관리자 사용자의 경우 기본 자격 증명과 함께 배송하거나 배포하지 마세요.

* 상위 10,000개 최악의 암호 목록에 대해 새 암호나 변경된 암호를 테스트하는 것과 같은 약한 암호 검사를 구현하세요.

* 새 계정 생성 및 암호 변경 중 알려진 침해된 자격 증명 목록에 대해 검증하세요(예: [haveibeenpwned.com](https://haveibeenpwned.com) 사용).

* 암호 길이, 복잡성 및 순환 정책을 [국가 표준 기술 연구소(National Institute of Standards and Technology, NIST) 800-63b의 섹션 5.1.1 가이드라인](https://pages.nist.gov/800-63-3/sp800-63b.html#:~:text=5.1.1%20Memorized%20Secrets)에 맞추세요. 기억된 비밀(Memorized Secrets) 또는 기타 현대적이고 증거 기반 암호 정책을 사용하세요.

* 침해가 의심되지 않는 한 사람에게 암호 순환을 강제하지 마세요. 침해가 의심되면 즉시 암호 재설정을 강제하세요. 

* 모든 결과에 대해 동일한 메시지("잘못된 사용자 이름 또는 암호.")를 사용하여 등록, 자격 증명 복구 및 API 경로를 계정 열거 공격에 대해 강화하세요.

* 실패한 로그인 시도를 제한하거나 점진적으로 지연시키되 서비스 거부 시나리오를 만들지 않도록 주의하세요. 모든 실패를 로깅하고 자격 증명 스터핑, 무차별 대입 또는 기타 공격이 탐지되거나 의심될 때 관리자에게 알림을 보내세요.

* 로그인 후 높은 엔트로피로 새로운 랜덤 세션 ID를 생성하는 서버 측, 안전한 내장 세션 관리자를 사용하세요. 세션 식별자는 URL에 있지 않아야 하며, 안전한 쿠키에 안전하게 저장되어야 하며, 로그아웃, 유휴 및 절대 타임아웃 후 무효화되어야 합니다. 

* 이상적으로는 인증, 신원 및 세션 관리를 처리하는 사전 제작된 잘 신뢰할 수 있는 시스템을 사용하세요. 가능할 때마다 강화되고 잘 테스트된 시스템을 구매하고 활용하여 이 위험을 전가하세요.


## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 자격 증명 스터핑, 알려진 사용자 이름과 암호 조합 목록 사용은 이제 매우 일반적인 공격입니다. 최근에 공격자는 일반적인 인간 행동을 기반으로 암호를 '증분'하거나 그렇지 않으면 조정하는 것으로 발견되었습니다. 예를 들어, 'Winter2025'를 'Winter2026'으로 변경하거나, 'ILoveMyDog6'을 'ILoveMyDog7' 또는 'ILoveMyDog5'로 변경합니다. 이러한 암호 시도 조정을 하이브리드 자격 증명 스터핑 공격 또는 암호 스프레이 공격이라고 하며, 전통적인 버전보다 더 효과적일 수 있습니다. 애플리케이션이 자동화된 위협(무차별 대입, 스크립트 또는 봇) 또는 자격 증명 스터핑에 대한 방어를 구현하지 않으면, 애플리케이션은 자격 증명이 유효한지 확인하고 무단 액세스를 얻기 위해 암호 오라클로 사용될 수 있습니다.

**시나리오 #2:** 대부분의 성공적인 인증 공격은 유일한 인증 요소로 암호를 계속 사용하기 때문에 발생합니다. 한때 모범 사례로 간주되었던 암호 순환 및 복잡성 요구 사항은 사용자가 암호를 재사용하고 약한 암호를 사용하도록 장려합니다. 조직은 NIST 800-63에 따라 이러한 관행을 중단하고 모든 중요한 시스템에서 다중 인증 사용을 강제하는 것이 권장됩니다.

**시나리오 #3:** 애플리케이션 세션 타임아웃이 올바르게 구현되지 않았습니다. 사용자가 공용 컴퓨터를 사용하여 애플리케이션에 액세스하고 "로그아웃"을 선택하는 대신, 사용자는 단순히 브라우저 탭을 닫고 떠납니다. 이것에 대한 또 다른 예는 단일 사인온(Single Sign-On, SSO) 세션이 단일 로그아웃(Single Logout, SLO)으로 닫을 수 없는 경우입니다. 즉, 단일 로그인이 예를 들어 메일 리더, 문서 시스템 및 채팅 시스템에 로그인합니다. 하지만 로그아웃은 현재 시스템에만 발생합니다. 공격자가 피해자가 성공적으로 로그아웃했다고 생각한 후 동일한 브라우저를 사용하지만 사용자가 일부 애플리케이션에 여전히 인증되어 있으면 피해자의 계정에 액세스할 수 있습니다. 민감한 애플리케이션이 제대로 종료되지 않고 동료가 잠금 해제된 컴퓨터에 (임시) 액세스할 수 있는 경우 사무실 및 기업에서도 동일한 문제가 발생할 수 있습니다.

## 참고 자료 (References). 

* [OWASP 인증 치트 시트 (OWASP Authentication Cheat Sheet)](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

* [OWASP 보안 코딩 관행 (OWASP Secure Coding Practices)](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/01-introduction/05-introduction)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-258 구성 파일의 빈 암호 (Empty Password in Configuration File)](https://cwe.mitre.org/data/definitions/258.html)

* [CWE-259 하드코딩된 암호 사용 (Use of Hard-coded Password)](https://cwe.mitre.org/data/definitions/259.html)

* [CWE-287 부적절한 인증 (Improper Authentication)](https://cwe.mitre.org/data/definitions/287.html)

* [CWE-288 대체 경로 또는 채널을 사용한 인증 우회 (Authentication Bypass Using an Alternate Path or Channel)](https://cwe.mitre.org/data/definitions/288.html)

* [CWE-289 대체 이름으로 인증 우회 (Authentication Bypass by Alternate Name)](https://cwe.mitre.org/data/definitions/289.html)

* [CWE-290 스푸핑으로 인증 우회 (Authentication Bypass by Spoofing)](https://cwe.mitre.org/data/definitions/290.html)

* [CWE-291 인증을 위한 IP 주소에 대한 의존 (Reliance on IP Address for Authentication)](https://cwe.mitre.org/data/definitions/291.html)

* [CWE-293 인증을 위한 Referer 필드 사용 (Using Referer Field for Authentication)](https://cwe.mitre.org/data/definitions/293.html)

* [CWE-294 캡처-재생으로 인증 우회 (Authentication Bypass by Capture-replay)](https://cwe.mitre.org/data/definitions/294.html)

* [CWE-295 부적절한 인증서 검증 (Improper Certificate Validation)](https://cwe.mitre.org/data/definitions/295.html)

* [CWE-297 호스트 불일치가 있는 인증서의 부적절한 검증 (Improper Validation of Certificate with Host Mismatch)](https://cwe.mitre.org/data/definitions/297.html)

* [CWE-298 호스트 불일치가 있는 인증서의 부적절한 검증 (Improper Validation of Certificate with Host Mismatch)](https://cwe.mitre.org/data/definitions/298.html)

* [CWE-299 호스트 불일치가 있는 인증서의 부적절한 검증 (Improper Validation of Certificate with Host Mismatch)](https://cwe.mitre.org/data/definitions/299.html)

* [CWE-300 비엔드포인트가 액세스할 수 있는 채널 (Channel Accessible by Non-Endpoint)](https://cwe.mitre.org/data/definitions/300.html)

* [CWE-302 가정된 불변 데이터로 인증 우회 (Authentication Bypass by Assumed-Immutable Data)](https://cwe.mitre.org/data/definitions/302.html)

* [CWE-303 인증 알고리즘의 잘못된 구현 (Incorrect Implementation of Authentication Algorithm)](https://cwe.mitre.org/data/definitions/303.html)

* [CWE-304 인증에서 중요한 단계 누락 (Missing Critical Step in Authentication)](https://cwe.mitre.org/data/definitions/304.html)

* [CWE-305 주요 약점으로 인증 우회 (Authentication Bypass by Primary Weakness)](https://cwe.mitre.org/data/definitions/305.html)

* [CWE-306 중요한 기능에 대한 인증 누락 (Missing Authentication for Critical Function)](https://cwe.mitre.org/data/definitions/306.html)

* [CWE-307 과도한 인증 시도의 부적절한 제한 (Improper Restriction of Excessive Authentication Attempts)](https://cwe.mitre.org/data/definitions/307.html)

* [CWE-308 단일 요소 인증 사용 (Use of Single-factor Authentication)](https://cwe.mitre.org/data/definitions/308.html)

* [CWE-309 기본 인증을 위한 암호 시스템 사용 (Use of Password System for Primary Authentication)](https://cwe.mitre.org/data/definitions/309.html)

* [CWE-346 원본 검증 오류 (Origin Validation Error)](https://cwe.mitre.org/data/definitions/346.html)

* [CWE-350 보안 중요 작업을 위한 역방향 DNS 해석에 대한 의존 (Reliance on Reverse DNS Resolution for a Security-Critical Action)](https://cwe.mitre.org/data/definitions/350.html)

* [CWE-384 세션 고정 (Session Fixation)](https://cwe.mitre.org/data/definitions/384.html)

* [CWE-521 약한 암호 요구 사항 (Weak Password Requirements)](https://cwe.mitre.org/data/definitions/521.html)

* [CWE-613 불충분한 세션 만료 (Insufficient Session Expiration)](https://cwe.mitre.org/data/definitions/613.html)

* [CWE-620 검증되지 않은 암호 변경 (Unverified Password Change)](https://cwe.mitre.org/data/definitions/620.html)

* [CWE-640 잊어버린 암호에 대한 약한 암호 복구 메커니즘 (Weak Password Recovery Mechanism for Forgotten Password)](https://cwe.mitre.org/data/definitions/640.html)

* [CWE-798 하드코딩된 자격 증명 사용 (Use of Hard-coded Credentials)](https://cwe.mitre.org/data/definitions/798.html)

* [CWE-940 통신 채널의 소스 검증 부적절 (Improper Verification of Source of a Communication Channel)](https://cwe.mitre.org/data/definitions/940.html)

* [CWE-941 통신 채널에서 잘못 지정된 대상 (Incorrectly Specified Destination in a Communication Channel)](https://cwe.mitre.org/data/definitions/941.html)

* [CWE-1390 약한 인증 (Weak Authentication)](https://cwe.mitre.org/data/definitions/1390.html)

* [CWE-1391 약한 자격 증명 사용 (Use of Weak Credentials)](https://cwe.mitre.org/data/definitions/1391.html)

* [CWE-1392 기본 자격 증명 사용 (Use of Default Credentials)](https://cwe.mitre.org/data/definitions/1392.html)

* [CWE-1393 기본 암호 사용 (Use of Default Password)](https://cwe.mitre.org/data/definitions/1393.html)

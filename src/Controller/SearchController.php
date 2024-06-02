<?php

namespace App\Controller;

use App\Form\SearchFormType;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SearchController extends AbstractController
{
    #[Route('/', name: 'app_search')]
    public function index(Request $request): Response
    {
        $form = $this->createForm(SearchFormType::class);
        $form->handleRequest($request);

        $results = [];
        if ($form->isSubmitted() && $form->isValid()) {
            $searchTerm = $form->getData()['item'];

            $jsonData = file_get_contents(__DIR__ . '/../../data.json');
            $dataArray = json_decode($jsonData, true);

            foreach ($dataArray as $data) {

                if (str_contains(strtolower($data['nom']), strtolower($searchTerm)) ||
                    str_contains(strtolower($data['prenom']), strtolower($searchTerm)) ||
                    str_contains(strtolower($data['email'][0]), strtolower($searchTerm))) {
                    $results[] = $data;
                }
            }
        }

        return $this->render('search/index.html.twig', [
            'form' => $form->createView(),
            'results' => $results
        ]);
    }
}